import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_text = ''
            for page in pdf.pages:
                
                all_text += page.extract_text() or ''
        return all_text
    except Exception as e:
        return f"Error reading PDF: {e}"

def calculate_resume_score(resume_text, job_description):
    resume_doc = nlp(resume_text.lower())
    job_doc = nlp(job_description.lower())

    resume_words = [word.text for word in resume_doc if word.pos_ in ['NOUN', 'VERB', 'ADJ']]
    job_words = [word.text for word in job_doc if word.pos_ in ['NOUN', 'VERB', 'ADJ']]

    resume_cleaned = ' '.join(resume_words)
    job_cleaned = ' '.join(job_words)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_cleaned, job_cleaned])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return score * 100