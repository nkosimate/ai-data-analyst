import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import OpenAI
import os
import plotly.express as px
import textwrap
from dotenv import load_dotenv

load_dotenv()



st.set_page_config(page_title="AI-Powered Data Analyst", layout="wide")
st.title("🤖 AI-Powered Data Analyst Assistant")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of your data")
    st.dataframe(df.head())

    query = st.text_input("💬 Ask a question about your data")

    if query:
        st.info("The assistant will analyse your query and respond shortly...")
        # Load your OpenAI key from environment
        try:
            openai_api_key = st.secrets["OPENAI_API_KEY"]
        except:
            openai_api_key = os.getenv("OPENAI_API_KEY")
        if openai_api_key is None:
            st.error("❌ OpenAI API key not found. Set OPENAI_API_KEY as an environment variable.")
        else:
            # Initialise LLM
            llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
            # Create an agent that understands Pandas data
            agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
            # Run the query through the agent
            with st.spinner("🧠 Thinking..."):
                response = agent.run(query)
                st.success("✅ Done!")
                st.markdown(response)

        # Basic keyword-based chart trigger
        chart_keywords = ["plot", "chart", "bar", "line", "histogram", "scatter","correlation"]
        if any(word in query.lower() for word in chart_keywords):
            with st.spinner("📊 Generating chart..."):

            # Special case: correlation heatmap
             if "correlation" in query.lower():
                numeric_df = df.select_dtypes(include='number')
                if numeric_df.empty:
                    st.warning("No numeric columns found to correlate.")
                else:
                    corr = numeric_df.corr()
                    fig = px.imshow(
                        corr,
                        text_auto=".2f",
                        color_continuous_scale="RdBu_r",
                        zmin=-1, zmax=1,
                        title="Correlation Heatmap"
                    )
                    st.plotly_chart(fig)

             else:
                # Ask the LLM for a Python code snippet that creates the chart
                chart_prompt = f"""
                Given this pandas dataframe:

                {df.head(3).to_markdown()}

                And the user's request: "{query}",

                Write a short Python code snippet using Plotly Express (imported as px)
                that creates the appropriate chart. The DataFrame is called 'df'.
                Do NOT show the chart — just return the code to create the figure and assign it to a variable called 'fig'.
                """
              
                raw_code = llm(chart_prompt)
                chart_code = textwrap.dedent(raw_code).strip()
                chart_code = chart_code.replace("return fig", "").replace("return", "")

                try:
                    # Evaluate the generated code to produce the figure
                    st.subheader("🧠 Chart Code from GPT")
                    st.code(chart_code, language="python")
                    global_env = {'df': df, 'px': px}
                    exec(chart_code, global_env)
                    fig = global_env.get("fig")
                    if fig:
                        st.plotly_chart(fig)
                    else:
                        st.error("❌ No figure was created by the generated code.")
                except Exception as e:
                    st.error(f"⚠️ Chart generation failed:\n\n{e}")
