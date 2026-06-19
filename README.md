#  Flask AI Content API

A lightweight Flask-based API that provides **AI-powered text summarization** and **blog generation** using modular NLP functions.

---

##  Features

- Text Summarization API – Converts long text into concise summaries  
- AI Blog Generator API – Generates blog content from a given topic  
- Fast JSON-based REST API  
- Modular structure (separate summarizer and generator logic)

---

## Tech Stack

- Python 
- Flask 
- JSON API
- Custom NLP modules (`summarizer.py`, `generator.py`)

---

##  Project Structure

```
lask-ai-content-api/
│
├── app.py # Main Flask application
├── summarizer.py # Text summarization logic
├── generator.py # Blog generation logic
└── README.md
```

---

##  API Endpoints

###  Summarize Text

**Endpoint:**

POST /summarize


**Request Body:**
```json
{
  "text": "Your long text goes here..."
}
```
Response:
``` json
{
  "summary": "Generated short summary..."
}
```
Generate Blog

Endpoint:


POST /blog


Request Body:
``` json

{
  "topic": "Artificial Intelligence in Education"
}
```
Response:
``` json
{
  "blog": "Generated blog content..."
}
```

How to Run Locally
1. Clone the repository
```bash
git clone https://github.com/your-username/flask-ai-content-api.git
cd flask-ai-content-api
```
3. Install dependencies
```bash
pip install flask
```
5. Run the app
```bash
python app.py
```
7. Open in browser
```
http://127.0.0.1:5000/
```
Testing Example

Summarize API
```
curl -X POST http://127.0.0.1:5000/summarize \
-H "Content-Type: application/json" \
-d '{"text":"Flask is a lightweight web framework..."}'
```
Blog API
```
curl -X POST http://127.0.0.1:5000/blog \
-H "Content-Type: application/json" \
-d '{"topic":"Future of AI"}'
```
Input must be valid JSON

##Author##
ADITHYA K S
