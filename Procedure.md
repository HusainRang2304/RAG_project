# How to Run (Procedure)
## Step 1 — Clone Repo
```
git clone <your-repo-url>
cd rag-knowledge-assistant
```
## Step 2 — Create Virtual Environment

Mac/Linux:
```
python -m venv venv
source venv/bin/activate
```
Windows:
```
python -m venv venv
venv\Scripts\activate
```

## Step 3 — Install Dependencies
```
pip install -r requirements.txt
```

## Step 4 — Add API Key
```
Create .env
OPENAI_API_KEY=your_key_here
```

## Step 5 — Add Documents

Put PDFs inside:
```
data/
```

Example:
```
data/aws_guide.pdf
data/company_policy.pdf
```

## Step 6 — Run App
```
streamlit run app.py
```
Browser opens automatically:
```
http://localhost:8501
```
