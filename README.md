# PhishGuard - Scam Email & URL Detection System

## Overview

PhishGuard is an AI-powered phishing detection system designed to identify malicious emails and suspicious URLs. The system leverages Machine Learning and Natural Language Processing (NLP) techniques to analyze email content and URLs, helping users detect phishing attempts and improve cybersecurity awareness.

## Features

* Phishing Email Detection

  * Analyzes email content and predicts whether it is legitimate or phishing.
* URL Safety Analysis

  * Detects suspicious and malicious URLs using machine learning models.
* NLP-Based Text Processing

  * Processes and extracts meaningful features from email text.
* User-Friendly Web Interface

  * Simple and intuitive interface for submitting emails and URLs.
* Real-Time Predictions

  * Provides instant results with confidence scores.
* Secure and Efficient

  * Designed to assist users in avoiding online scams and phishing attacks.

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning & NLP

* Scikit-learn
* Pandas
* NumPy
* NLTK
* TF-IDF Vectorization

### Dataset

* Public phishing email datasets
* Malicious and legitimate URL datasets

## System Architecture

1. User submits an email or URL.
2. Input data is preprocessed.
3. Relevant features are extracted.
4. Machine learning model analyzes the input.
5. Prediction is generated.
6. Result is displayed to the user.

## Project Structure

```text
PhishGuard/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── email_detection.html
│   └── url_detection.html
│
├── models/
│   ├── email_model.pkl
│   └── url_model.pkl
│
├── datasets/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/ShivaSaiAnmol/PhishGuard---Scam-Email-Url-Detection-System.git
cd PhishGuard---Scam-Email-Url-Detection-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Machine Learning Workflow

* Data Collection
* Data Cleaning
* Feature Extraction
* TF-IDF Vectorization
* Model Training
* Model Evaluation
* Deployment using Flask

## Results

The system successfully identifies phishing emails and malicious URLs, helping users make safer decisions online and reducing the risk of cyber attacks.


## Acknowledgements

* Flask Documentation
* Scikit-learn Documentation
* NLTK Documentation
* Open-source phishing datasets and cybersecurity research resources
