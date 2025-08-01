import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import os

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
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key is None:
            st.error("❌ OpenAI API key not found. Set OPENAI_API_KEY as an environment variable.")
        else:
            # Initialise LLM
            llm = OpenAI(temperature=0, openai_api_key=openai_key)
            # Create an agent that understands Pandas data
            agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
            # Run the query through the agent
            with st.spinner("🧠 Thinking..."):
                response = agent.run(query)
                st.success("✅ Done!")
                st.markdown(response)
