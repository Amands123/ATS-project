# ATS Gemini Pro 🚀

<img width="1363" height="540" alt="image" src="https://github.com/user-attachments/assets/3834b12f-4280-49ed-a5d3-00f280d7b907" />


ATS Gemini Pro is an AI-powered Applicant Tracking System (ATS) Resume Analyzer built using Streamlit and Google Gemini AI. The application helps job seekers evaluate their resumes against job descriptions, identify missing skills and keywords, generate ATS match scores, create cover letters, and prepare for interviews.

## Features

* 📄 Resume Analysis against Job Descriptions
* 🎯 ATS Match Score Calculation
* 🔍 Missing Keywords Identification
* 💡 Resume Optimization Suggestions
* 📝 AI-Generated Cover Letters
* 🎤 Interview Question Generation
* 📊 Detailed ATS Evaluation Report
* 📥 PDF Report Download
* ☁️ Deployable on AWS EC2
* 🤖 Powered by Google Gemini 2.5 Flash

---

## Architecture

AWS EC2 (Ubuntu) hosts the Streamlit application while Google Gemini AI provides the intelligence for resume evaluation and content generation.

```text
User
  │
  ▼
AWS EC2 (Streamlit Application)
  │
  ▼
Google Gemini AI (Gemini 2.5 Flash)
  │
  ▼
ATS Analysis Results
```

---

## Prerequisites

* AWS EC2 Ubuntu Server (20.04 or later)
* Python 3.10+
* Git
* Google Gemini API Key
* Poppler Utilities

---

## AWS EC2 Setup

### Step 1: Launch EC2 Instance

Create an Ubuntu EC2 instance and ensure the following inbound ports are open:

| Port | Protocol | Purpose               |
| ---- | -------- | --------------------- |
| 22   | TCP      | SSH Access            |
| 8501 | TCP      | Streamlit Application |

---

### Step 2: Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

### Step 3: Install Python and Virtual Environment

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

### Step 4: Install Git

```bash
sudo apt install git -y
```

Verify:

```bash
git --version
```

---

### Step 5: Install Poppler

Required for PDF processing.

```bash
sudo apt install poppler-utils -y
```

Verify:

```bash
pdftotext -v
```

---

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/ATS_Gemini_Pro.git

cd ATS_Gemini_Pro
```

---

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## Google Gemini AI Setup

### Step 1: Generate API Key

Create a Gemini API key from Google AI Studio:

https://aistudio.google.com/apikey

---

### Step 2: Configure Streamlit Secrets

Create the directory:

```bash
mkdir -p .streamlit
```

Create the secrets file:

```bash
vi .streamlit/secrets.toml
```

Add:

```toml
GOOGLE_API_KEY = "your-gemini-api-key"
```

---

## Run Application

```bash
streamlit run app.py --server.port 8501 --server.enableCORS false
```

Application URL:

```text
http://<EC2-Public-IP>:8501
```

Example:

```text
http://52.xxx.xxx.xxx:8501
```

---

## Project Structure

```text
ATS_Gemini_Pro/
│
├── app.py
├── requirements.txt
├── README.md
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── reports/
├── logs/
└── assets/
```

---

## Security Best Practices

Never commit:

```text
.streamlit/secrets.toml
```

Add the following to `.gitignore`:

```text
.streamlit/secrets.toml
__pycache__/
*.pyc
venv/
.env
```

---

## Future Enhancements

* Resume Optimization Engine
* Multi-Resume Comparison
* Job Recommendation Engine
* LinkedIn Profile Analysis
* Dashboard Analytics
* Docker Deployment
* CI/CD Pipeline Integration
* AWS ECS Deployment

---

## Technology Stack

* Python
* Streamlit
* Google Gemini 2.5 Flash
* PyMuPDF
* ReportLab
* AWS EC2
* Git & GitHub

---

## Author

Aman Agarwal

AWS | DevOps | Data Engineering | AI Automation

---

## License

This project is licensed under the MIT License.
