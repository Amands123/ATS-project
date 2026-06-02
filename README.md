_# ATS Gemini Pro

Part 1 AWS Ubuntu EC2 instance:
Launch a new EC2 instance
Ubuntu Server 20.04 LTS
Allowing essential port i.e 8501

Part-2 Application installation 
Step-1 update & Install Python 3.7+ and pip

sudo -i
sudo apt update && sudo apt install python3 python3-pip python3-venv -y

Step-2  Install Git  sudo apt install git -y
Step-3 Install Poppler (for pdf2image)
       sudo apt install poppler-utils -y
Step-4 Set Up a Virtual Environment
 python3 -m venv venv
 source venv/bin/activate

Step-5 Install Project Dependencies
 pip install --upgrade pip
 pip install -r requirements.txt

AWS + GCP + AI ATS System

Part 3 AI Gemini Setup 

Get Gemini API Key from Google AI Studio

Part-4 Connect AWS ATS application with GCP Gemini AI
 
1.Add the API Key to Streamlit Secrets
mkdir -p .streamlit
vi .streamlit/secrets.toml

GOOGLE_API_KEY = "your-api-key-here"

2.Run the Streamlit App

streamlit run app.py --server.port 8501 --server.enableCORS false
_
