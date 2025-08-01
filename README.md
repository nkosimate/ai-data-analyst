🤖 AI-Powered Data Analyst Assistant

Ever wished you had a data-savvy AI teammate who could instantly answer questions like:

“What’s the churn rate by contract type?”
“Plot average call duration per customer.”
“Which features matter most for customer churn?”

Welcome to your new data sidekick.

Built with ❤️ using LangChain, OpenAI, Streamlit, and Plotly, this project turns CSV files into interactive, intelligent dashboards with natural language querying, automatic insights, and visualisations.

⸻

🚀 Features

✨ Upload your CSV file — and the AI handles the rest
🧠 Ask questions in plain English (no SQL, no code)
📊 Automatically generate beautiful Plotly charts
💬 Supports basic analysis, trends, correlations, and more
🔒 Local-first: your data stays on your machine
⚡️ Supercharged with OpenAI + LangChain agents

⸻

🧪 Example Use Cases
	•	“What percentage of customers churned last month?”
	•	“Create a box plot of CustServCalls by Churn.”
	•	“Show the top 5 states with the highest total charge.”
	•	“What’s the correlation between call minutes and churn?”

⸻

🛠️ Stack
Tech                    Why we love it
🧠 OpenAI               For powerful, conversational understanding
🦜 LangChain            Orchestrates natural language to action
📊 Plotly               Gorgeous interactive charts
🌐 Streamlit            Fast, friendly UI for data apps
🐍 Python               The glue holding it all together

📂 Getting Started
git clone https://github.com/nkosimate/ai-data-analyst.git
cd ai-data-analyst
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Then create a .env file:
OPENAI_API_KEY=your-key-here

And finally:
streamlit run app.py
📁 Sample Dataset

I recommend starting with something like telecom_churn.csv from https://www.kaggle.com/datasets/barun2104/telecom-churn/data , but feel free to upload any tabular CSV. The assistant will do its best to interpret your data automatically!

⸻

🎯 Future Enhancements
	•	✅ Natural language → SQL → insight queries
	•	📈 Auto-generated data profiling summaries
	•	💡 Smart visualisation suggestions
	•	🔍 Drill-down insights and trends over time
	•	🗂️ Multi-file support and memory

⸻

👨🏽‍💻 Made By

Built with curiosity and code by Nkosi Mate 👨🏽‍💻
Powered by open source. Fuelled by coffee. ☕

⸻

⭐️ Star This Repo

If you like this project, please consider giving it a ⭐️!
It helps others discover this fun and powerful tool.

