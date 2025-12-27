# Deployment Guide

AI Health Copilot Pro - Production Deployment Instructions

Copyright (c) 2025 Harry Patria - Patria & Co.
Agentic AI Masterclass Project

---

## Quick Deployment Checklist

- [ ] Environment variables configured
- [ ] Model files in `models/` directory
- [ ] Datasets in `datasets/` directory
- [ ] Logo in `assets/` directory
- [ ] OpenAI API key obtained
- [ ] Docker installed (for containerized deployment)
- [ ] Git repository initialized
- [ ] .gitignore configured
- [ ] Security review completed

---

## Deployment Options

### 1. Local Development Deployment

**Prerequisites:**
- Python 3.9+
- pip package manager

**Steps:**

```bash
# Clone repository
git clone https://github.com/Harrypatria/ml_health_chatbot.git
cd ml_health_chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run application
streamlit run app.py
```

**Access:** http://localhost:8501

---

### 2. Docker Deployment

**Prerequisites:**
- Docker installed and running

**Steps:**

```bash
# Build Docker image
docker build -t ai-health-copilot:1.0.0 .

# Run container
docker run -d \
  --name ai-health-copilot \
  -p 8501:8501 \
  -e OPENAI_API_KEY=your_api_key_here \
  ai-health-copilot:1.0.0

# Check logs
docker logs -f ai-health-copilot

# Stop container
docker stop ai-health-copilot

# Remove container
docker rm ai-health-copilot
```

**Access:** http://localhost:8501

---

### 3. Docker Compose Deployment

**Prerequisites:**
- Docker and Docker Compose installed

**Steps:**

```bash
# Configure environment
cp config/.env.example .env
# Edit .env file with your configuration

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Restart services
docker-compose restart

# Rebuild and restart
docker-compose up -d --build
```

**Access:** http://localhost:8501

---

### 4. Cloud Platform Deployments

#### A. Streamlit Community Cloud (Free Tier)

**Steps:**

1. Push code to GitHub repository
2. Visit https://share.streamlit.io
3. Connect GitHub account
4. Select repository and branch
5. Configure secrets:
   - Add `OPENAI_API_KEY` in Secrets section
6. Click "Deploy"

**Limitations:**
- Limited resources
- Public deployment
- Community support only

#### B. AWS EC2 Deployment

**Steps:**

```bash
# 1. Launch EC2 instance (Ubuntu 20.04 LTS recommended)
# 2. SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# 3. Install Docker
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# 4. Clone repository
git clone https://github.com/Harrypatria/ml_health_chatbot.git
cd ml_health_chatbot

# 5. Configure environment
cp config/.env.example .env
nano .env  # Add OPENAI_API_KEY

# 6. Deploy with Docker Compose
docker-compose up -d

# 7. Configure nginx reverse proxy (optional)
sudo apt-get install nginx
# Configure nginx to proxy port 80 to 8501

# 8. Setup SSL with Let's Encrypt (optional)
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

**Access:** http://your-ec2-ip:8501 or https://yourdomain.com

#### C. Google Cloud Run Deployment

**Steps:**

```bash
# 1. Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# 2. Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# 3. Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ai-health-copilot

# 4. Deploy to Cloud Run
gcloud run deploy ai-health-copilot \
  --image gcr.io/YOUR_PROJECT_ID/ai-health-copilot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=your_key \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300

# 5. Get service URL
gcloud run services describe ai-health-copilot --region us-central1
```

**Access:** Provided Cloud Run URL

#### D. Azure Container Instances

**Steps:**

```bash
# 1. Install Azure CLI
# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

# 2. Login to Azure
az login

# 3. Create resource group
az group create --name ai-health-copilot-rg --location eastus

# 4. Build and push to Azure Container Registry
az acr create --resource-group ai-health-copilot-rg \
  --name aihealthcopilotacr --sku Basic

az acr build --registry aihealthcopilotacr \
  --image ai-health-copilot:1.0.0 .

# 5. Deploy to Container Instances
az container create \
  --resource-group ai-health-copilot-rg \
  --name ai-health-copilot \
  --image aihealthcopilotacr.azurecr.io/ai-health-copilot:1.0.0 \
  --dns-name-label ai-health-copilot \
  --ports 8501 \
  --environment-variables OPENAI_API_KEY=your_key
```

**Access:** http://ai-health-copilot.eastus.azurecontainer.io:8501

---

## Production Configuration

### Environment Variables

Create `.env` file in project root:

```env
# OpenAI
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4

# Application
APP_VERSION=1.0.0
DEBUG_MODE=False
LOG_LEVEL=INFO

# Performance
ENABLE_LATENCY_TRACKING=True
MAX_RESPONSE_TIME_MS=3000
```

### Streamlit Secrets (for Streamlit Cloud)

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-your-actual-key-here"
OPENAI_MODEL = "gpt-4"
```

---

## Security Hardening

### 1. API Key Protection

```bash
# Never commit .env files
echo ".env" >> .gitignore

# Use secrets management
# AWS: AWS Secrets Manager
# GCP: Secret Manager
# Azure: Key Vault
```

### 2. Network Security

```bash
# Configure firewall
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
sudo ufw enable

# Use SSL/TLS
# Install certbot for Let's Encrypt
sudo certbot --nginx -d yourdomain.com
```

### 3. Container Security

```dockerfile
# Run as non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Scan for vulnerabilities
docker scan ai-health-copilot:1.0.0
```

---

## Monitoring and Logging

### Application Logs

```bash
# Docker logs
docker logs -f ai-health-copilot

# Docker Compose logs
docker-compose logs -f

# Save logs to file
docker logs ai-health-copilot > app.log 2>&1
```

### Health Checks

```bash
# Check application health
curl http://localhost:8501/_stcore/health

# Docker health check
docker inspect --format='{{.State.Health.Status}}' ai-health-copilot
```

### Performance Monitoring

Monitor these metrics:
- Response time (latency)
- Memory usage
- CPU utilization
- API call frequency
- Error rates

---

## Backup and Recovery

### Backup Strategy

```bash
# 1. Backup models
tar -czf models-backup-$(date +%Y%m%d).tar.gz models/

# 2. Backup datasets
tar -czf datasets-backup-$(date +%Y%m%d).tar.gz datasets/

# 3. Backup configuration
cp .env .env.backup.$(date +%Y%m%d)

# 4. Upload to cloud storage
# AWS S3
aws s3 cp models-backup-*.tar.gz s3://your-bucket/backups/

# Google Cloud Storage
gsutil cp models-backup-*.tar.gz gs://your-bucket/backups/
```

### Recovery Procedure

```bash
# 1. Download backup
aws s3 cp s3://your-bucket/backups/models-backup-20250127.tar.gz .

# 2. Extract
tar -xzf models-backup-20250127.tar.gz

# 3. Restart application
docker-compose restart
```

---

## Scaling Strategies

### Horizontal Scaling

```yaml
# docker-compose.yml
services:
  ai-health-copilot:
    deploy:
      replicas: 3

# Load balancer configuration required
```

### Vertical Scaling

```yaml
# Increase resources
services:
  ai-health-copilot:
    deploy:
      resources:
        limits:
          cpus: '4.0'
          memory: 4G
```

---

## Troubleshooting

### Common Issues

**Issue: Container fails to start**
```bash
# Check logs
docker logs ai-health-copilot

# Verify environment variables
docker exec ai-health-copilot env | grep OPENAI
```

**Issue: High latency**
```bash
# Check resource usage
docker stats ai-health-copilot

# Increase resources in docker-compose.yml
```

**Issue: API errors**
```bash
# Test OpenAI connection
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Maintenance

### Regular Tasks

**Weekly:**
- Review application logs
- Check API usage and costs
- Monitor performance metrics

**Monthly:**
- Update dependencies
- Review security advisories
- Backup models and data
- Test disaster recovery

**Quarterly:**
- Security audit
- Performance optimization
- Update documentation
- Review and retrain models

---

## Support

For deployment issues:
- Check GitHub Issues
- Review documentation
- Contact: Repository discussions

---

**Last Updated:** 2025-01-27
**Version:** 1.0.0
**Maintained by:** Harry Patria - Patria & Co.
