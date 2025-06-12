# 📄 ResumeRanker

ResumeRanker is an AI-powered Django web application that matches and ranks uploaded resumes based on a specific job description using NLP and machine learning techniques like TF-IDF and cosine similarity.

## 🚀 Features

- Upload job descriptions and resumes
- Rank resumes based on job relevance
- Simple web frontend with backend API
- PDF text extraction using `pdfplumber`
- NLP processing with spaCy
- TF-IDF scoring and cosine similarity via scikit-learn

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- spaCy (NLP)
- pdfplumber (PDF text extraction)
- scikit-learn (ML)
- HTML/CSS (for frontend)

## 📦 Setup Instructions

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/resumeranker.git
    cd resumeranker
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download spaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

5. Run the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000/` to access the frontend.

## 📁 Folder Structure

