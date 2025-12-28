# AI Health Copilot Pro 
## Masterclass Batch 6 Agentic AI and RAG, December 2025

Advanced Multi-Disease Prediction System powered by Machine Learning and Generative AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)](https://streamlit.io)

---

## Overview

AI Health Copilot Pro is an enterprise-grade health analytics platform that leverages machine learning algorithms to predict multiple disease risks including Diabetes, Cardiovascular Disease, and Parkinson's Disease. The system integrates OpenAI's GPT-4 for intelligent health recommendations and features real-time latency monitoring for optimal performance.

**Developed by:** Harry Patria - Patria & Co.
**Program:** Agentic AI Masterclass
**Version:** 1.0.0
**License:** MIT

---

## Key Features

- **Multi-Disease Prediction**: Three specialized ML models for comprehensive health assessment
- **AI-Powered Insights**: OpenAI GPT-4 integration for personalized health recommendations
- **Performance Monitoring**: Real-time latency tracking (ms-level precision)
- **Modern UI/UX**: Dark/light theme support with responsive design
- **Personalized Health Planning**: Custom dietary and fitness recommendations
- **Enterprise-Ready**: Docker support, comprehensive documentation, and production-grade architecture

---

## Technology Stack

| Category | Technology | Version |
|----------|-----------|---------|
| Frontend Framework | Streamlit | 1.31.0 |
| ML Framework | Scikit-learn | 1.4.0 |
| AI Integration | OpenAI API | 1.12.0 |
| Data Processing | Pandas, NumPy | 2.2.0, 1.26.3 |
| Containerization | Docker | Latest |
| Version Control | Git | Latest |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│            (Streamlit UI + Performance Monitoring)          │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                   Business Logic Layer                       │
│     (Disease Prediction + AI Analysis + Health Planning)    │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                      Data Layer                              │
│         (ML Models + Datasets + Model Metadata)             │
└─────────────────────────────────────────────────────────────┘
```

For detailed architecture documentation, see [STRUCTURE.txt](./STRUCTURE.txt)

---

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git
- OpenAI API key (for AI-powered features)
- Docker (optional, for containerized deployment)

### Installation

#### Method 1: Local Installation (Recommended for Development)

1. **Clone the Repository**
```bash
git clone https://github.com/Harrypatria/ml_health_chatbot.git
cd ml_health_chatbot
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Configure Environment Variables**
```bash
# Create .env file
cp config/.env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_api_key_here
```

5. **Run the Application**
```bash
streamlit run app.py
```

6. **Access the Application**
Open your browser and navigate to: `http://localhost:8501`

#### Method 2: Docker Deployment (Recommended for Production)

1. **Clone the Repository**
```bash
git clone https://github.com/Harrypatria/ml_health_chatbot.git
cd ml_health_chatbot
```

2. **Build Docker Image**
```bash
docker build -t ai-health-copilot:latest .
```

3. **Run Container**
```bash
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_api_key_here \
  ai-health-copilot:latest
```

4. **Access the Application**
Open your browser and navigate to: `http://localhost:8501`

#### Method 3: Docker Compose (Full Stack Deployment)

1. **Configure Environment**
```bash
cp config/.env.example .env
# Edit .env with your configuration
```

2. **Start Services**
```bash
docker-compose up -d
```

3. **View Logs**
```bash
docker-compose logs -f
```

4. **Stop Services**
```bash
docker-compose down
```

---

## Usage Guide

### 1. Disease Prediction

#### Diabetes Prediction
- Navigate to "Diabetes Prediction" from the sidebar
- Enter patient parameters (glucose, BMI, blood pressure, etc.)
- Click "Analyze Diabetes Risk"
- View prediction results and latency metrics
- Review AI-powered health recommendations (requires API key)

#### Heart Disease Prediction
- Navigate to "Heart Disease Prediction"
- Input cardiovascular parameters (cholesterol, ECG results, etc.)
- Click "Analyze Heart Disease Risk"
- Review comprehensive risk assessment

#### Parkinson's Disease Prediction
- Navigate to "Parkinsons Prediction"
- Enter voice analysis parameters
- Click "Analyze Parkinson's Risk"
- View neurological health assessment

### 2. Personalized Health Planning
- Navigate to "Personalized Health Plan"
- Complete your health profile (age, weight, height, activity level)
- Select dietary preferences and fitness goals
- Click "Generate My Personalized Plan"
- Receive custom dietary and fitness recommendations

### 3. Performance Monitoring
- All predictions display three latency metrics:
  - **Model Prediction Latency**: Time for ML inference
  - **AI Analysis Latency**: Time for GPT-4 response generation
  - **Total Operation Latency**: End-to-end processing time

---

## API Configuration

### Obtaining OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/signup/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new secret key
5. Copy the key (shown only once)
6. Add to `.env` file or enter in the application sidebar

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4

# Application Configuration
APP_TITLE=AI Health Copilot Pro
APP_VERSION=1.0.0
DEBUG_MODE=False

# Performance Settings
ENABLE_LATENCY_TRACKING=True
MAX_RESPONSE_TIME_MS=3000
```

---

## Model Information

### Diabetes Prediction Model
- **Algorithm**: Logistic Regression / Random Forest
- **Dataset**: Pima Indians Diabetes Database
- **Features**: 8 clinical parameters
- **Performance**: Training accuracy documented in analytics notebooks

### Heart Disease Prediction Model
- **Algorithm**: Support Vector Machine / Random Forest
- **Dataset**: UCI Heart Disease Dataset
- **Features**: 13 cardiovascular parameters
- **Performance**: Cross-validated metrics available in notebooks

### Parkinson's Disease Prediction Model
- **Algorithm**: XGBoost / Random Forest
- **Dataset**: Oxford Parkinson's Disease Detection Dataset
- **Features**: 22 voice biomarkers
- **Performance**: Comprehensive evaluation in analytics notebooks

For model training details, see the `analytics/` directory.

---

## Project Structure

```
ml_health_chatbot/
├── app.py                      # Main application entry point
├── assets/                     # Static resources
│   └── logo.png
├── models/                     # Trained ML models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── datasets/                   # Training datasets
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
├── analytics/                  # Jupyter notebooks
│   ├── diabetes_analysis.ipynb
│   ├── heart_disease_analysis.ipynb
│   └── parkinsons_analysis.ipynb
├── docs/                       # Documentation
├── config/                     # Configuration files
├── tests/                      # Unit tests
├── .gitignore                  # Git ignore rules
├── .dockerignore               # Docker ignore rules
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container setup
├── requirements.txt            # Python dependencies
├── STRUCTURE.txt               # Architecture documentation
├── LICENSE                     # MIT License
├── VERSION                     # Version file
└── README.md                   # This file
```

---

## Development Workflow

### Setting Up Development Environment

1. **Fork the Repository**
```bash
# On GitHub, click "Fork" button
git clone https://github.com/YOUR_USERNAME/ml_health_chatbot.git
cd ml_health_chatbot
```

2. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Install Development Dependencies**
```bash
pip install -r requirements.txt
```

4. **Make Changes and Test**
```bash
# Run application
streamlit run app.py

# Run tests (when available)
pytest tests/

# Code formatting
black app.py

# Linting
flake8 app.py
```

5. **Commit and Push**
```bash
git add .
git commit -m "feat: description of your changes"
git push origin feature/your-feature-name
```

6. **Create Pull Request**
- Navigate to GitHub repository
- Click "New Pull Request"
- Select your feature branch
- Describe changes and submit

### Code Quality Standards

- **Formatting**: Use `black` for code formatting
- **Linting**: Pass `flake8` checks
- **Type Hints**: Use type annotations where applicable
- **Documentation**: Add docstrings for all functions
- **Testing**: Write unit tests for new features

---

## Deployment Guide

### GitHub Repository Setup

1. **Create GitHub Repository**
```bash
# Initialize Git (if not already done)
git init

# Add remote
git remote add origin https://github.com/Harrypatria/ml_health_chatbot.git

# Stage all files
git add .

# Commit
git commit -m "Initial commit: AI Health Copilot Pro v1.0.0"

# Push to GitHub
git push -u origin master
```

2. **Repository Settings**
- Add repository description
- Add topics: `machine-learning`, `healthcare`, `streamlit`, `ai`, `openai`, `health-analytics`
- Add README preview
- Enable Issues for bug tracking
- Enable Discussions for community engagement

3. **Branch Protection** (Optional)
- Navigate to Settings > Branches
- Add rule for `master` branch
- Enable "Require pull request reviews before merging"
- Enable "Require status checks to pass before merging"

### Docker Hub Deployment

1. **Build and Tag Image**
```bash
docker build -t harrypatria/ai-health-copilot:1.0.0 .
docker tag harrypatria/ai-health-copilot:1.0.0 harrypatria/ai-health-copilot:latest
```

2. **Push to Docker Hub**
```bash
docker login
docker push harrypatria/ai-health-copilot:1.0.0
docker push harrypatria/ai-health-copilot:latest
```

3. **Pull and Run**
```bash
docker pull harrypatria/ai-health-copilot:latest
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key harrypatria/ai-health-copilot:latest
```

### Cloud Deployment Options

#### Streamlit Community Cloud (Free)
1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Add secrets (OpenAI API key)
5. Deploy

#### AWS EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Install Docker
sudo yum update -y
sudo yum install docker -y
sudo service docker start

# Pull and run container
sudo docker pull harrypatria/ai-health-copilot:latest
sudo docker run -d -p 80:8501 -e OPENAI_API_KEY=your_key harrypatria/ai-health-copilot:latest
```

#### Google Cloud Run
```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ai-health-copilot

# Deploy to Cloud Run
gcloud run deploy ai-health-copilot \
  --image gcr.io/YOUR_PROJECT_ID/ai-health-copilot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=your_key
```

---

## Performance Optimization

### Latency Targets
- Model Prediction: < 50ms
- AI Analysis: < 2000ms (dependent on OpenAI API)
- Total Operation: < 3000ms

### Optimization Strategies
1. **Model Caching**: Models loaded once at startup
2. **Session State**: Efficient state management
3. **Async Operations**: Non-blocking API calls
4. **Resource Pooling**: Reuse connections
5. **CDN Integration**: Static asset delivery

---

## Security Best Practices

1. **API Key Management**
   - Never commit API keys to repository
   - Use environment variables or secrets management
   - Rotate keys regularly

2. **Input Validation**
   - All user inputs validated and sanitized
   - Range checks on numeric inputs
   - Type enforcement

3. **Data Privacy**
   - No persistent storage of user health data
   - Session-based architecture
   - HIPAA compliance considerations

4. **Dependency Management**
   - Regular security audits
   - Automated vulnerability scanning
   - Keep dependencies updated

---

## Troubleshooting

### Common Issues

#### Issue: "Model files not found"
**Solution**: Ensure model files are in the `models/` directory
```bash
ls models/
# Should show: diabetes_model.sav, heart_disease_model.sav, parkinsons_model.sav
```

#### Issue: "OpenAI API authentication error"
**Solution**: Verify API key is correct and active
```bash
# Test API key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

#### Issue: "Port 8501 already in use"
**Solution**: Change port or kill existing process
```bash
# Change port
streamlit run app.py --server.port 8502

# Or kill existing process (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Or kill existing process (macOS/Linux)
lsof -ti:8501 | xargs kill -9
```

#### Issue: Docker container won't start
**Solution**: Check logs and environment variables
```bash
docker logs <container_id>
docker inspect <container_id>
```

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Areas
- Model improvements and new disease predictions
- UI/UX enhancements
- Performance optimizations
- Documentation improvements
- Bug fixes
- Test coverage

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Harry Patria - Patria & Co.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## Acknowledgments

- **Scikit-learn** community for excellent ML tools
- **Streamlit** team for the amazing web framework
- **OpenAI** for GPT-4 API access
- Dataset contributors from UCI ML Repository and Kaggle

---

## Roadmap

### Version 1.1.0 (Planned)
- [ ] Additional disease prediction models
- [ ] Multi-language support
- [ ] PDF report generation
- [ ] Historical data tracking
- [ ] Advanced analytics dashboard

### Version 1.2.0 (Planned)
- [ ] User authentication and profiles
- [ ] Doctor/Patient portal
- [ ] Telemedicine integration
- [ ] Mobile application
- [ ] Real-time monitoring

---

## Contact & Support

**Project Owner**: Harry Patria
**Organization**: Patria & Co.
**Program**: Agentic AI Masterclass
**Repository**: [https://github.com/Harrypatria/ml_health_chatbot](https://github.com/Harrypatria/ml_health_chatbot)

For questions, issues, or collaboration inquiries:
- Open an issue on GitHub
- Submit a pull request
- Contact via repository discussions

---

## Disclaimer

This application is designed for educational and informational purposes as part of the Agentic AI Masterclass. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding medical conditions.

---

**Built with excellence by Harry Patria - Patria & Co.**

*Empowering healthcare through AI and machine learning*
