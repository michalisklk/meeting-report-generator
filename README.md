# Meeting Report Generator

This is a small project I built using Python, Streamlit and the Gemini API.

The goal is simple: instead of manually organizing meeting notes, the user can paste a transcript (or upload a text file) and generate a structured follow-up report automatically.

## What the app does

* Accepts meeting notes as text input
* Supports uploading `.txt` files
* Generates a structured meeting report
* Identifies key discussion points
* Extracts tasks and deadlines
* Highlights possible risks and next steps

## Technologies

* Python
* Streamlit
* Gemini API
* python-dotenv

## How to run

Clone the repository:

```bash
git clone https://github.com/michalisklk/meeting-report-generator.git
cd meeting-report-generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run Main.py
```

## Why I built it

I wanted to experiment with Large Language Models and explore a practical business use case. This project shows how AI can help automate repetitive documentation tasks and make meeting follow-ups faster and more organized.

## Author

Michail Kolokotsios
