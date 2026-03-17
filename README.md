# AI Data Analyst

Ask questions about your CSV data in plain English. Get charts back.

That's mostly it. No SQL, no Python, no pivot tables. You upload a file, type something like *"which states have the highest average charge?"*, and the assistant figures out what you meant and plots it.

Built with LangChain, OpenAI, Streamlit, and Plotly.


## What it can do

- Answer questions about your data in natural language
- Generate interactive Plotly charts on demand
- Handle correlation questions, distributions, group comparisons, and basic trends
- Keep your data local — nothing leaves your machine

It works best with clean tabular CSVs. The messier the data, the more it'll struggle, same as any analyst would.


## Example questions

These are things I've tested against the telecom churn dataset:

- *"What percentage of customers churned?"*
- *"Create a box plot of customer service calls by churn status."*
- *"Show the top 5 states by total charge."*
- *"Is there a correlation between call minutes and churn?"*

Your dataset will have different columns, but the assistant will read the schema and try to interpret your questions against it automatically.

---

## Stack

| Tool | What it does |
|------|-------------|
| OpenAI | Understands your questions |
| LangChain | Turns those questions into actions |
| Plotly | Renders the charts |
| Streamlit | The UI |
| Python | Glue |

---

## Getting started

```bash
git clone https://github.com/nkosimate/ai-data-analyst.git
cd ai-data-analyst
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the root:

```
OPENAI_API_KEY=your-key-here
```

Then run it:

```bash
streamlit run app.py
```

---

## Sample dataset

I'd recommend starting with the [Telecom Churn dataset on Kaggle](https://www.kaggle.com/datasets/barun2104/telecom-churn/data). It's clean, well-structured, and most of the example questions above were written against it.

Any tabular CSV should work though. The assistant reads the column names and data types on upload.

---

## What's next

A few things I want to add:

- Auto-generated data profile summaries on upload
- Smarter chart type suggestions based on the question
- Multi-file support
- Memory across questions in a session

---

## Made by

[Nkosi Mate](https://github.com/nkosimate)

If this is useful to you, a star helps other people find it.
