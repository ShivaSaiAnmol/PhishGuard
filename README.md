# 🛡️ PhishGuard

## AI-Powered Scam Email & Malicious URL Detection System

> **Protecting users from phishing attacks through intelligent URL verification and AI-driven email threat analysis.**

---

## 🚨 Why PhishGuard?

Every day, cybercriminals send millions of phishing emails and create fraudulent websites designed to steal sensitive information such as passwords, banking credentials, and personal data.

The challenge is that many phishing attempts closely resemble legitimate communications, making them difficult to identify manually.

**PhishGuard** was built to solve this problem by providing automated threat detection and risk assessment for both URLs and email content.

---

## 🎯 Project Overview

PhishGuard is a cybersecurity-focused web application that helps users identify potentially dangerous websites and scam emails before interacting with them.

By combining Google's threat intelligence with AI-powered content analysis, the system evaluates suspicious inputs and generates a detailed threat assessment.

---

## ✨ Core Features

### 🌐 Malicious URL Detection

Analyze suspicious links using Google's Safe Browsing database.

**Capabilities:**

* Detect phishing websites
* Identify malware-hosting URLs
* Flag deceptive domains
* Verify website safety

---

### 📧 Email Threat Analysis

Analyze email content using AI and NLP techniques.

**Detects:**

* Phishing attempts
* Credential harvesting requests
* Fake login pages
* Financial scams
* Urgency-based social engineering attacks

---

### 📊 Risk Score Generation

Each analysis generates a risk score based on multiple threat indicators.

```text
Risk Score: 0 – 100

0 - 30    → Safe ✅
31 - 70   → Suspicious ⚠️
71 - 100  → Malicious 🚨
```

---

### 📝 Threat Classification

Results are categorized as:

🟢 Safe

🟡 Suspicious

🔴 Malicious

---

### 📄 Detailed Security Reports

Users receive:

* Threat level
* Risk score
* Detected indicators
* Security recommendations

---

## ⚙️ System Workflow

```text
                    User Input
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
      URL Input                  Email Content
          │                             │
          ▼                             ▼
 Google Safe Browsing         Gemini AI Analysis
          │                             │
          ▼                             ▼
 Threat Detection           NLP Processing
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 Risk Assessment
                         │
                         ▼
                Threat Classification
                         │
                         ▼
          Safe / Suspicious / Malicious
```

---

## 🔍 Detection Indicators

### URL Analysis

The system checks:

* Known phishing URLs
* Malware-hosting websites
* Unsafe domains
* Blacklisted websites
* Threat intelligence databases

### Email Analysis

The system looks for:

* Urgent language
* Account suspension threats
* Password reset scams
* Fake login requests
* Credential theft attempts
* Financial fraud indicators
* Suspicious sender behavior

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### APIs & AI

* Google Safe Browsing API
* Gemini API

### Database

* SQLite / MongoDB

### Development Tools

* Git
* GitHub

---

## 📂 Project Structure

```text
PhishGuard/
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── templates/
│   ├── index.html
│   ├── url_analysis.html
│   └── email_analysis.html
│
├── app.py
├── config.py
├── requirements.txt
├── database.db
└── README.md
```

---

## 📸 Sample Analysis

### URL Check

```text
Input URL:
https://secure-bank-login-update.xyz

Threat Analysis:
• Domain flagged as phishing
• Unsafe reputation detected

Risk Score:
92/100

Result:
🚨 MALICIOUS
```

---

### Email Analysis

```text
Subject:
URGENT: Verify Your Account

Threat Indicators:
• Urgency tactics detected
• Credential request identified
• Suspicious login link found

Risk Score:
89/100

Result:
🚨 PHISHING EMAIL
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/PhishGuard.git
cd PhishGuard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Keys

Add your:

* Google Safe Browsing API Key
* Gemini API Key

inside your configuration file.

### Run Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## 🎓 What I Learned

This project helped me gain hands-on experience in:

* Cybersecurity Fundamentals
* Threat Intelligence Integration
* REST API Integration
* Natural Language Processing
* AI-Powered Content Analysis
* Flask Web Development
* Risk Assessment Systems
* Software Testing & Debugging

---

## 🔮 Future Enhancements

### 🧩 Browser Extension

Real-time website scanning while browsing.

### 🤖 Advanced AI Models

Use LLMs and transformer-based models for deeper threat analysis.

### 📱 Mobile Application

Threat detection on smartphones.

### ☁️ Cloud Deployment

Deploy using AWS, Azure, or Google Cloud.

### 📊 Security Analytics Dashboard

Track phishing trends and threat statistics.

---

## ⭐ Support the Project

If you found this project useful:

⭐ Star the Repository

🍴 Fork the Project

🚀 Contribute New Features


