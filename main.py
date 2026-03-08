from flask import Flask, render_template, request
import google.generativeai as genai
import os
import PyPDF2
from dotenv import load_dotenv
import requests # New Import for API Calls
import json # New Import for API Calls

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# --- CRITICAL FIX: Get the API Keys from the environment ---
# Gemini API Key for content analysis
GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")
# Safe Browsing API Key for high-accuracy URL detection
SAFE_BROWSING_API_KEY = os.environ.get("GOOGLE_SAFE_BROWSING_API_KEY")
SAFE_BROWSING_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

if not GEMINI_API_KEY:
    # We must have the Gemini key for content analysis
    raise ValueError("GOOGLE_API_KEY not found. Please ensure it is set in your .env file.")

# Set up the Google API Key and configure genai
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# functions
def predict_fake_or_real_email_content(text):
    prompt = f"""
    You are an expert in identifying scam messages in text, email etc. Analyze the given text and classify it as:

    - **Real/Legitimate** (Authentic, safe message)
    - **Scam/Fake** (Phishing, fraud, or suspicious message)

    **for the following Text:**
    {text}

    **Return a clear message indicating whether this content is real or a scam. 
    If it is a scam, mention why it seems fraudulent. If it is real, state that it is legitimate.**

    **Only return the classification message and nothing else.**
    Note: Don't return empty or null, you only need to return message for the input text
    """

    response = model.generate_content(prompt)
    return response.text.strip() if response else "Classification failed."


def safe_browsing_check(url):
    """Checks URL against Google Safe Browsing API for known threats."""
    if not SAFE_BROWSING_API_KEY:
        print("Warning: Safe Browsing API key not configured. Falling back to LLM for URL check.")
        return None

    # Reverting to the most specific and reliable threat types for high confidence results
    threat_types = [
        "MALWARE", 
        "SOCIAL_ENGINEERING", 
        "UNWANTED_SOFTWARE",
    ]

    payload = {
        "client": {
            # Use a dummy client info since this is a local app
            "clientId": "your-flask-app", 
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": threat_types,
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(
            f"{SAFE_BROWSING_URL}?key={SAFE_BROWSING_API_KEY}",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status() # Raise exception for bad status codes (4xx or 5xx)

        matches = response.json().get("matches")
        
        if matches:
            # If matches exist, the URL is unsafe. 
            # Use the threatType from the first match for the most relevant classification.
            threat_type = matches[0].get("threatType", "UNKNOWN_THREAT").replace("_", " ").title()
            
            # Map the common Social Engineering/Phishing threat type to a clean label
            if threat_type in ["Social Engineering"]:
                return "Unsafe - Phishing/Scam (Safe Browsing Check)"
            
            # For all other known threats (Malware, Unwanted Software, etc.)
            return f"Unsafe - {threat_type} (Safe Browsing Check)"
        else:
            # No matches means the URL is considered safe
            return "Benign/Safe (Safe Browsing Check)"

    except requests.exceptions.RequestException as e:
        print(f"Safe Browsing API Error: {e}")
        # Return None to signal a fallback to the LLM
        return None
    except Exception as e:
        print(f"An unexpected error occurred during Safe Browsing check: {e}")
        return None


def url_detection(url):
    """Determines URL safety using Safe Browsing first, then falling back to LLM."""
    
    # 1. Try Safe Browsing API for high accuracy
    classification = safe_browsing_check(url)
    
    if classification is not None:
        # Safe Browsing gave us a definitive answer
        return classification
    
    # 2. Fallback to Gemini LLM if Safe Browsing failed or was unavailable
    print("Falling back to LLM classification...")
    prompt = f"""
    You are an advanced AI model specializing in URL security classification. Analyze the given URL and classify it as one of the following categories:

    1. benign**: Safe, trusted, and non-malicious websites.
    2. phishing**: Fraudulent websites designed to steal personal information.
    3. malware**: URLs that distribute viruses, ransomware, or malicious software.
    4. defacement**: Hacked or defaced websites.

    **Input URL:** {url}

    **Output Format:**  
    - Return only a single lowercase class name (e.g., 'benign', 'phishing', 'malware', 'defacement')
    - Do not return any other text, explanation, or punctuation.
    """

    response = model.generate_content(prompt)
    
    llm_result = response.text.strip().lower() if response else "detection failed"
    # Clean up the LLM result to only take the first word (the classification) and capitalize it
    clean_llm_result = llm_result.split()[0].title() if llm_result.split() else "Failed"
    return f"{clean_llm_result} (LLM Fallback)"


# Routes

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/scam/', methods=['POST'])
def detect_scam():
    if 'file' not in request.files:
        return render_template("index.html", message="No file uploaded.")

    file = request.files['file']
    extracted_text = ""

    if file.filename.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        except Exception as e:
            return render_template("index.html", message=f"Error reading PDF file: {e}")

    elif file.filename.endswith('.txt'):
        try:
            extracted_text = file.read().decode("utf-8")
        except:
            return render_template("index.html", message="Error reading TXT file.")
            
    else:
        return render_template("index.html", message="Invalid file type. Please upload a PDF or TXT file.")

    if not extracted_text.strip():
        return render_template("index.html", message="File is empty or text could not be extracted.")

    # Call the LLM to classify content
    message = predict_fake_or_real_email_content(extracted_text)
    
    return render_template("index.html", message=message, detection_type="scam_email")


@app.route('/predict', methods=['POST'])
def predict_url():
    url = request.form.get('url', '').strip()

    if not url.startswith(("http://", "https://")):
        # We need to render the input field so the user sees what they typed
        return render_template("index.html", url_error="Invalid URL format. Must start with http:// or https://", input_url=url)

    # Call the specialized URL detection function
    classification = url_detection(url)
    
    return render_template("index.html", input_url=url, predicted_class=classification, detection_type="url_check")


if __name__ == '__main__':
    # You should set debug=False for production
    app.run(debug=True)
