# API Documentation

AI Health Copilot Pro - API Integration Guide

Copyright (c) 2025 Harry Patria - Patria & Co.
Agentic AI Masterclass Project

---

## Overview

This document provides comprehensive documentation for integrating with external APIs used in the AI Health Copilot Pro application.

## OpenAI API Integration

### Configuration

The application uses OpenAI's GPT-4 API for generating intelligent health recommendations and insights.

#### API Key Setup

1. **Obtain API Key**
   - Visit https://platform.openai.com/signup/
   - Create account or sign in
   - Navigate to API Keys section
   - Generate new secret key

2. **Configure in Application**

   **Option 1: Environment Variables**
   ```bash
   export OPENAI_API_KEY="sk-your-api-key-here"
   ```

   **Option 2: .env File**
   ```env
   OPENAI_API_KEY=sk-your-api-key-here
   OPENAI_MODEL=gpt-4
   ```

   **Option 3: Streamlit Secrets**
   ```toml
   # .streamlit/secrets.toml
   OPENAI_API_KEY = "sk-your-api-key-here"
   ```

### API Endpoints Used

#### Chat Completions API

**Endpoint:** `https://api.openai.com/v1/chat/completions`

**Request Format:**
```python
{
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "You are a helpful medical assistant."},
        {"role": "user", "content": "User query here"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}
```

**Response Format:**
```python
{
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "gpt-4",
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "AI response here"
        },
        "finish_reason": "stop"
    }],
    "usage": {
        "prompt_tokens": 56,
        "completion_tokens": 31,
        "total_tokens": 87
    }
}
```

### Usage in Application

#### Disease Risk Analysis

```python
def generate_openai_response(prompt, api_key, model="gpt-4"):
    """Generate response using OpenAI Chat API."""
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
```

#### Prompt Templates

**Diabetes Analysis Prompt:**
```
Based on these diabetes risk factors:
- Pregnancies: {value}
- Glucose: {value} mg/dL
- Blood Pressure: {value} mmHg
- BMI: {value} kg/m²
- Age: {value} years

The prediction is: {diagnosis}

Provide a clear explanation of the key risk factors and actionable health
recommendations in 3 concise paragraphs.
```

**Heart Disease Analysis Prompt:**
```
Based on these cardiovascular risk factors:
- Age: {value} years, Sex: {value}
- Cholesterol: {value} mg/dl
- Blood Pressure: {value} mmHg
- Max Heart Rate: {value} bpm

The prediction is: {diagnosis}

Provide a clear explanation of the key risk factors and actionable
cardiovascular health recommendations in 3 concise paragraphs.
```

**Personalized Health Plan Prompt:**
```
Create a personalized daily meal plan for:
Age: {age} years
Weight: {weight}kg
Height: {height}cm
BMI: {bmi}
Activity Level: {activity_level}
Dietary Preferences: {preferences}
Fitness Goals: {goals}

Include specific meals, portion sizes, calories, and why this plan works
for their goals.
```

### Rate Limits

- **GPT-4**: 200 requests per minute (RPM)
- **Tokens per minute (TPM)**: 40,000 for GPT-4

### Error Handling

```python
try:
    response = generate_openai_response(prompt, api_key)
except openai.AuthenticationError:
    # Handle authentication error
    error_message = "Invalid API key"
except openai.RateLimitError:
    # Handle rate limit
    error_message = "Rate limit exceeded"
except openai.APIError as e:
    # Handle API error
    error_message = f"OpenAI API error: {e}"
except Exception as e:
    # Handle other errors
    error_message = f"Unexpected error: {e}"
```

### Cost Optimization

1. **Caching Responses**
   - Cache common queries
   - Store previous analyses

2. **Token Management**
   - Limit max_tokens parameter
   - Use concise prompts
   - Implement streaming for long responses

3. **Model Selection**
   - Use GPT-3.5-turbo for simpler queries
   - Reserve GPT-4 for complex analysis

### Security Best Practices

1. **API Key Management**
   - Never commit API keys to version control
   - Use environment variables
   - Rotate keys regularly
   - Monitor usage on OpenAI dashboard

2. **Input Validation**
   - Sanitize all user inputs
   - Validate prompt lengths
   - Implement rate limiting

3. **Error Messages**
   - Don't expose API keys in error messages
   - Log errors securely
   - Provide user-friendly error messages

## Future API Integrations

### Planned Integrations

1. **Health Data APIs**
   - Apple HealthKit
   - Google Fit
   - Fitbit API

2. **Medical Databases**
   - PubMed API
   - FDA Drug Database
   - Clinical Trials API

3. **Telemedicine APIs**
   - Zoom Healthcare API
   - Twilio Video API
   - Doxy.me API

4. **Analytics APIs**
   - Google Analytics
   - Mixpanel
   - Segment

### Integration Guidelines

1. **Authentication**
   - Use OAuth 2.0 where available
   - Store credentials securely
   - Implement token refresh

2. **Data Privacy**
   - Comply with HIPAA regulations
   - Encrypt data in transit and at rest
   - Implement user consent flows

3. **Performance**
   - Implement caching
   - Use async requests
   - Handle timeouts gracefully

## API Testing

### Test OpenAI Connection

```bash
# Test API key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Test from Python

```python
import openai

client = openai.OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello, World!"}
    ]
)

print(response.choices[0].message.content)
```

## Monitoring and Analytics

### Tracking API Usage

1. **OpenAI Dashboard**
   - Monitor token usage
   - Track costs
   - View usage patterns

2. **Application Metrics**
   - Log API response times
   - Track success/failure rates
   - Monitor latency

3. **Alerts**
   - Set up cost alerts
   - Monitor rate limit warnings
   - Track error rates

## Support and Resources

### OpenAI Resources
- Documentation: https://platform.openai.com/docs
- API Reference: https://platform.openai.com/docs/api-reference
- Community: https://community.openai.com
- Status Page: https://status.openai.com

### Contact
For API-related issues:
- Check OpenAI status page
- Review error logs
- Contact OpenAI support
- Refer to GitHub issues

---

**Last Updated:** 2025-01-27
**Version:** 1.0.0
**Maintained by:** Harry Patria - Patria & Co.
