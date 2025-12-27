# Quick Start Guide

AI Health Copilot Pro - Get Started in 5 Minutes

Copyright (c) 2025 Harry Patria - Patria & Co.

---

## Prerequisites

- Python 3.9+ installed
- Git installed
- OpenAI API key (get from https://platform.openai.com)

---

## Installation (3 Steps)

### Step 1: Clone Repository
```bash
git clone https://github.com/Harrypatria/ml_health_chatbot.git
cd ml_health_chatbot
```

### Step 2: Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 3: Configure & Run
```bash
# Add your OpenAI API key (or enter in app sidebar)
export OPENAI_API_KEY="sk-your-key-here"

# Run application
streamlit run app.py
```

**Open browser:** http://localhost:8501

---

## Docker Quick Start (2 Steps)

### Step 1: Build
```bash
docker build -t ai-health-copilot .
```

### Step 2: Run
```bash
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=sk-your-key-here \
  ai-health-copilot
```

**Open browser:** http://localhost:8501

---

## Using the Application

### Disease Prediction
1. Select prediction type from sidebar
2. Enter health parameters
3. Click "Analyze Risk"
4. View results and latency metrics
5. Get AI-powered recommendations

### Health Planning
1. Navigate to "Personalized Health Plan"
2. Enter your profile information
3. Select preferences and goals
4. Click "Generate My Personalized Plan"
5. Review custom recommendations

---

## Next Steps

- Read full [README.md](README.md) for detailed documentation
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
- Check [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) for API details
- See [STRUCTURE.txt](STRUCTURE.txt) for architecture overview

---

## Support

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Documentation: Repository Wiki

---

**Ready to deploy? See DEPLOYMENT.md for cloud platform guides.**
