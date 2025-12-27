"""
AI Health Copilot Pro
Advanced Multi-Disease Prediction System

Copyright (c) 2026 Harry Patria - Patria & Co.
Licensed under MIT License

Agentic AI Masterclass Project
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import openai
import base64
import time
import json
from datetime import datetime
import hashlib

# Set page configuration
st.set_page_config(
    page_title="AI Health Copilot Pro | Agentic AI Masterclass",
    layout="wide",
    page_icon="⚕",
    initial_sidebar_state="expanded"
)

# Authentication Configuration
AUTH_USERNAME = "masterclass"
AUTH_PASSWORD = "agentic26"

def hash_password(password):
    """Hash password for secure comparison"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_authentication(username, password):
    """Verify user credentials"""
    return username == AUTH_USERNAME and hash_password(password) == hash_password(AUTH_PASSWORD)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ''
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Toggle dark mode function
def toggle_dark_mode():
    """Toggle between light and dark mode"""
    st.session_state.dark_mode = not st.session_state.dark_mode

# Performance monitoring class
class PerformanceMonitor:
    """Monitor and track application performance metrics"""

    @staticmethod
    def display_latency(latency_ms, operation_name="Operation"):
        """Display latency metrics in professional format"""
        dark_mode = st.session_state.get('dark_mode', False)

        bg_color = 'rgba(66, 99, 235, 0.15)' if dark_mode else 'rgba(66, 99, 235, 0.08)'
        text_color = '#e2e8f0' if dark_mode else '#4b5563'
        accent_color = '#818cf8' if dark_mode else '#6366f1'

        st.markdown(
            f"""
            <div style='background: {bg_color};
                        padding: 0.75rem 1.25rem; border-radius: 8px; margin: 0.5rem 0;
                        border-left: 3px solid {accent_color};'>
                <p style='margin: 0; font-size: 0.875rem; color: {text_color}; font-weight: 500;'>
                    {operation_name} Runtime: <span style='color: {accent_color}; font-weight: 600;'>{latency_ms:.2f} ms</span>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Professional CSS - GESTALT principles, Blue/Purple gradient, Light/Dark mode support
def load_professional_css():
    dark_mode = st.session_state.get('dark_mode', False)

    if dark_mode:
        # Dark mode color scheme
        colors = {
            'primary-gradient': 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
            'secondary-gradient': 'linear-gradient(135deg, #818cf8 0%, #a78bfa 100%)',
            'bg-primary': '#0f172a',
            'bg-secondary': '#1e293b',
            'bg-tertiary': '#334155',
            'text-primary': '#f1f5f9',
            'text-secondary': '#cbd5e1',
            'text-accent': '#818cf8',
            'border-color': '#334155',
            'shadow-sm': '0 1px 2px 0 rgba(0, 0, 0, 0.3)',
            'shadow-md': '0 4px 6px -1px rgba(0, 0, 0, 0.4)',
            'shadow-lg': '0 10px 15px -3px rgba(0, 0, 0, 0.5)',
            'input-bg': '#1e293b',
            'card-bg': '#1e293b',
            'sidebar-bg': 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)',
        }
    else:
        # Light mode color scheme
        colors = {
            'primary-gradient': 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)',
            'secondary-gradient': 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
            'bg-primary': '#ffffff',
            'bg-secondary': '#f8fafc',
            'bg-tertiary': '#f1f5f9',
            'text-primary': '#1e293b',
            'text-secondary': '#64748b',
            'text-accent': '#6366f1',
            'border-color': '#e2e8f0',
            'shadow-sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
            'shadow-md': '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
            'shadow-lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
            'input-bg': '#f8fafc',
            'card-bg': '#ffffff',
            'sidebar-bg': 'linear-gradient(180deg, #f8fafc 0%, #ffffff 100%)',
        }

    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* GESTALT Principle: Proximity and Continuity - Dynamic Theme */
    :root {{
        --primary-gradient: {colors['primary-gradient']};
        --secondary-gradient: {colors['secondary-gradient']};
        --bg-primary: {colors['bg-primary']};
        --bg-secondary: {colors['bg-secondary']};
        --bg-tertiary: {colors['bg-tertiary']};
        --text-primary: {colors['text-primary']};
        --text-secondary: {colors['text-secondary']};
        --text-accent: {colors['text-accent']};
        --border-color: {colors['border-color']};
        --shadow-sm: {colors['shadow-sm']};
        --shadow-md: {colors['shadow-md']};
        --shadow-lg: {colors['shadow-lg']};
        --input-bg: {colors['input-bg']};
        --card-bg: {colors['card-bg']};
        --sidebar-bg: {colors['sidebar-bg']};
    }}

    /* GESTALT Principle: Figure/Ground - Clear background */
    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }}

    /* Main container - GESTALT: Proximity */
    .main .block-container {{
        padding: 2rem 3rem !important;
        max-width: 1400px !important;
        background-color: var(--bg-primary) !important;
    }}

    /* GESTALT Principle: Similarity - Consistent styling */
    h1, h2, h3 {{
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.025em !important;
    }}

    h1 {{
        font-size: 2.25rem !important;
        margin-bottom: 0.5rem !important;
    }}

    h2 {{
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
    }}

    h3 {{
        font-size: 1.25rem !important;
        margin-bottom: 0.75rem !important;
    }}

    /* Professional Card Design - GESTALT: Closure */
    .professional-card {{
        background: var(--card-bg);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-md);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .professional-card:hover {{
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }}

    /* Input Fields - Minimalist Design */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextInput input,
    .stNumberInput input {{
        background-color: var(--input-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.9375rem !important;
        transition: all 0.2s ease !important;
    }}

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stTextInput input:focus,
    .stNumberInput input:focus {{
        border-color: var(--text-accent) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
        outline: none !important;
        background-color: var(--card-bg) !important;
    }}

    /* Professional Button Design */
    .stButton > button {{
        background: var(--primary-gradient) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.9375rem !important;
        letter-spacing: 0.025em !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow-md) !important;
        width: 100% !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-lg) !important;
        opacity: 0.95 !important;
    }}

    /* Sidebar - Professional Design */
    .css-1d391kg, [data-testid="stSidebar"] {{
        background: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border-color) !important;
    }}

    /* Sidebar text color */
    [data-testid="stSidebar"] * {{
        color: var(--text-primary) !important;
    }}

    /* Success/Error/Warning Messages - Clean Design */
    .stSuccess {{
        background-color: rgba(16, 185, 129, 0.1) !important;
        border-left: 4px solid #10b981 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        color: #065f46 !important;
    }}

    .stError {{
        background-color: rgba(239, 68, 68, 0.1) !important;
        border-left: 4px solid #ef4444 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        color: #991b1b !important;
    }}

    .stWarning {{
        background-color: rgba(245, 158, 11, 0.1) !important;
        border-left: 4px solid #f59e0b !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        color: #92400e !important;
    }}

    .stInfo {{
        background-color: rgba(59, 130, 246, 0.1) !important;
        border-left: 4px solid #3b82f6 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        color: #1e40af !important;
    }}

    /* Selectbox - Professional Styling */
    .stSelectbox > div > div,
    .stSelectbox select {{
        background-color: var(--input-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }}

    .stSelectbox option {{
        background-color: var(--input-bg) !important;
        color: var(--text-primary) !important;
    }}

    /* Label Styling */
    .stTextInput > label,
    .stNumberInput > label,
    .stSelectbox > label,
    label {{
        font-weight: 500 !important;
        color: var(--text-primary) !important;
        font-size: 0.875rem !important;
        margin-bottom: 0.5rem !important;
    }}

    /* Metric Display */
    .metric-card {{
        background: var(--card-bg);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        text-align: center;
        box-shadow: var(--shadow-sm);
    }}

    /* Welcome Page Sections */
    .welcome-section {{
        background: var(--card-bg);
        border-radius: 16px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-md);
    }}

    .welcome-hero {{
        background: var(--primary-gradient);
        color: white;
        border-radius: 16px;
        padding: 3rem;
        margin-bottom: 2rem;
        text-align: center;
    }}

    .feature-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }}

    .feature-card {{
        background: var(--bg-secondary);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }}

    .feature-card:hover {{
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--text-accent);
    }}

    /* Theme toggle button */
    .theme-toggle-btn {{
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 1000;
        background: var(--card-bg);
        border: 2px solid var(--border-color);
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
        font-size: 1.25rem;
    }}

    .theme-toggle-btn:hover {{
        transform: scale(1.1);
        box-shadow: var(--shadow-lg);
        border-color: var(--text-accent);
    }}

    /* Hide Streamlit default elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Professional footer */
    .app-footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: var(--card-bg);
        border-top: 1px solid var(--border-color);
        color: var(--text-secondary);
        text-align: center;
        padding: 0.75rem 0;
        font-size: 0.875rem;
        z-index: 100;
    }}

    /* Responsive design */
    @media (max-width: 768px) {{
        .main .block-container {{
            padding: 1rem !important;
        }}

        .professional-card {{
            padding: 1.5rem;
        }}

        .welcome-hero {{
            padding: 2rem;
        }}

        h1 {{
            font-size: 1.75rem !important;
        }}

        .theme-toggle-btn {{
            width: 45px;
            height: 45px;
            font-size: 1.1rem;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load professional CSS
load_professional_css()

# Authentication Page
def show_login_page():
    """Display professional login interface"""
    st.markdown("""
        <div class="welcome-hero">
            <h1 style="color: white; font-size: 2.5rem; margin-bottom: 1rem;">AI Health Copilot Pro</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.125rem; margin-bottom: 0;">
                Advanced Multi-Disease Prediction System
            </p>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.875rem; margin-top: 0.5rem;">
                Powered by Machine Learning & Generative AI
                Dr Harry Patria - Chief Data AI at Patria & Co.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown("### Authentication Required")
        st.markdown("Please enter your credentials to access the system")

        username = st.text_input("Username", placeholder="Enter username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Enter password", key="login_password")

        if st.button("Sign In", key="login_button"):
            if check_authentication(username, password):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

        st.markdown("---")
        st.markdown("""
            <p style='text-align: center; color: #64748b; font-size: 0.875rem;'>
                Agentic AI Masterclass Project<br>
                Copyright © 2026 Harry Patria - Patria & Co.
            </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Welcome Page with Problem-Solution Framework
def show_welcome_page():
    """Display professional welcome page highlighting problem, solution, technology, and users"""

    st.markdown("""
        <div class="welcome-hero">
            <h1 style="color: white; font-size: 2.5rem; margin-bottom: 1rem;">AI Health Copilot Pro</h1>
            <p style="color: rgba(255,255,255,0.95); font-size: 1.25rem; margin-bottom: 0.5rem;">
                Transforming Healthcare Through Intelligent Disease Prediction
            </p>
            <p style="color: rgba(255,255,255,0.85); font-size: 1rem;">
                Enterprise-Grade Health Analytics Platform
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Problem Statement
    st.markdown('<div class="welcome-section">', unsafe_allow_html=True)
    st.markdown("## The Challenge")
    st.markdown("""
        <p style='font-size: 1.125rem; line-height: 1.7; color: #475569;'>
        Healthcare systems worldwide face critical challenges in early disease detection and risk assessment.
        Traditional diagnostic approaches often identify conditions at advanced stages, resulting in:
        </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3 style="color: #ef4444; margin-bottom: 0.5rem;">Delayed Diagnosis</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Late-stage disease identification increases treatment complexity and costs
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3 style="color: #f59e0b; margin-bottom: 0.5rem;">Limited Accessibility</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Geographic and economic barriers restrict access to preventive health screening
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-card">
                <h3 style="color: #8b5cf6; margin-bottom: 0.5rem;">Resource Constraints</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Healthcare professionals face overwhelming patient volumes and limited diagnostic tools
                </p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Solution
    st.markdown('<div class="welcome-section">', unsafe_allow_html=True)
    st.markdown("## Our Solution")
    st.markdown("""
        <p style='font-size: 1.125rem; line-height: 1.7; color: #475569; margin-bottom: 1.5rem;'>
        AI Health Copilot Pro leverages advanced machine learning algorithms and generative AI to provide
        rapid, accurate disease risk assessment and personalized health recommendations.
        </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <h2 style="color: #6366f1; margin: 0;">3</h2>
                <p style="color: #64748b; margin-top: 0.5rem; font-weight: 500;">Disease Predictions</p>
                <p style="color: #94a3b8; font-size: 0.875rem;">Diabetes, Heart Disease, Parkinson's</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="metric-card">
                <h2 style="color: #8b5cf6; margin: 0;">&lt;50ms</h2>
                <p style="color: #64748b; margin-top: 0.5rem; font-weight: 500;">Prediction Latency</p>
                <p style="color: #94a3b8; font-size: 0.875rem;">Real-time risk assessment</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="metric-card">
                <h2 style="color: #6366f1; margin: 0;">AI-Powered</h2>
                <p style="color: #64748b; margin-top: 0.5rem; font-weight: 500;">Health Insights</p>
                <p style="color: #94a3b8; font-size: 0.875rem;">Personalized recommendations</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Technology Stack
    st.markdown('<div class="welcome-section">', unsafe_allow_html=True)
    st.markdown("## Technology Architecture")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3 style="color: #6366f1; margin-bottom: 1rem;">Machine Learning Engine</h3>
                <ul style="color: #64748b; line-height: 1.8;">
                    <li>Scikit-learn 1.4.0 framework</li>
                    <li>Multiple algorithm ensemble</li>
                    <li>Cross-validated models</li>
                    <li>Real-time inference optimization</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="feature-card" style="margin-top: 1rem;">
                <h3 style="color: #8b5cf6; margin-bottom: 1rem;">Data Processing</h3>
                <ul style="color: #64748b; line-height: 1.8;">
                    <li>Pandas & NumPy pipeline</li>
                    <li>Feature engineering</li>
                    <li>Input validation & sanitization</li>
                    <li>Performance monitoring</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3 style="color: #6366f1; margin-bottom: 1rem;">AI Integration</h3>
                <ul style="color: #64748b; line-height: 1.8;">
                    <li>OpenAI GPT-4 API</li>
                    <li>Natural language insights</li>
                    <li>Personalized health plans</li>
                    <li>Contextual recommendations</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="feature-card" style="margin-top: 1rem;">
                <h3 style="color: #8b5cf6; margin-bottom: 1rem;">Infrastructure</h3>
                <ul style="color: #64748b; line-height: 1.8;">
                    <li>Streamlit web framework</li>
                    <li>Docker containerization</li>
                    <li>Production-ready deployment</li>
                    <li>Scalable architecture</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Target Users
    st.markdown('<div class="welcome-section">', unsafe_allow_html=True)
    st.markdown("## Who Benefits")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="feature-card" style="text-align: center;">
                <h3 style="color: #6366f1; margin-bottom: 0.75rem;">Healthcare Professionals</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Clinical decision support and rapid screening tools
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-card" style="text-align: center;">
                <h3 style="color: #8b5cf6; margin-bottom: 0.75rem;">Patients</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Accessible preventive health screening and personalized guidance
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-card" style="text-align: center;">
                <h3 style="color: #6366f1; margin-bottom: 0.75rem;">Researchers</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Disease pattern analysis and predictive modeling insights
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="feature-card" style="text-align: center;">
                <h3 style="color: #8b5cf6; margin-bottom: 0.75rem;">Health Systems</h3>
                <p style="color: #64748b; font-size: 0.9375rem;">
                    Population health management and resource optimization
                </p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Call to Action
    st.markdown('<div class="welcome-section" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown("## Get Started")
    st.markdown("""
        <p style='font-size: 1.125rem; color: #475569; margin-bottom: 2rem;'>
        Select a prediction module from the sidebar to begin your health assessment
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Display logo in sidebar with high fidelity
def display_logo():
    """Display application logo from assets directory with high fidelity and resolution"""
    logo_paths = ["assets/Logo.png", "Logo.png", "assets/logo.png", "logo.png"]
    dark_mode = st.session_state.get('dark_mode', False)

    # Box shadow based on theme
    shadow = '0 4px 12px rgba(0, 0, 0, 0.4)' if dark_mode else '0 4px 12px rgba(0, 0, 0, 0.15)'
    border = '2px solid rgba(139, 92, 246, 0.3)' if dark_mode else '2px solid rgba(99, 102, 241, 0.2)'

    for logo_path in logo_paths:
        try:
            with open(logo_path, "rb") as f:
                img_base64 = base64.b64encode(f.read()).decode("utf-8")
            st.sidebar.markdown(
                f'''<div style="text-align:center; margin-bottom: 1.5rem; padding: 1rem;">
                    <img src="data:image/png;base64,{img_base64}"
                         width="200"
                         style="border-radius: 16px;
                                box-shadow: {shadow};
                                border: {border};
                                image-rendering: -webkit-optimize-contrast;
                                image-rendering: crisp-edges;
                                max-width: 100%;
                                height: auto;">
                </div>''',
                unsafe_allow_html=True
            )
            return
        except FileNotFoundError:
            continue
        except Exception as e:
            break

    # Fallback to text-based logo
    bg_gradient = 'linear-gradient(135deg, #6366f1, #8b5cf6)'
    st.sidebar.markdown(
        f'''<div style="text-align:center; margin-bottom: 1.5rem; padding: 1.5rem;
                        background: {bg_gradient}; border-radius: 16px;
                        color: white; font-weight: 700; font-size: 1.25rem;
                        box-shadow: {shadow}; letter-spacing: 0.5px;">
            AI Health Copilot Pro
        </div>''',
        unsafe_allow_html=True
    )

# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models with fallback
try:
    diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open(f'{working_dir}/models/parkinsons_model.sav', 'rb'))
except FileNotFoundError:
    try:
        diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
        heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
        parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
    except:
        st.error("Model files not found. Please ensure model files are in the 'models' directory.")
except Exception as e:
    st.error(f"Error loading models: {str(e)}")

# OpenAI response generation
def generate_openai_response(prompt, api_key, model="gpt-4"):
    """Generate response using OpenAI Chat API"""
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a professional medical assistant. Provide clear, evidence-based health insights."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Enhanced input field with tooltips
def professional_input_field(label, min_val, max_val, default_val, key, help_text, unit=""):
    """Create professional input field with tooltip"""
    field_label = f"{label}"
    if unit:
        field_label += f" ({unit})"

    return st.number_input(
        field_label,
        min_value=min_val,
        max_value=max_val,
        value=default_val,
        key=key,
        help=help_text,
        format="%.2f" if isinstance(default_val, float) else "%d"
    )

# Default values for normal health conditions
NORMAL_DEFAULTS = {
    'diabetes': {
        'pregnancies': 2, 'glucose': 120, 'blood_pressure': 80, 'skin_thickness': 20,
        'insulin': 80, 'bmi': 25.0, 'pedigree': 0.5, 'age': 50
    },
    'heart': {
        'age': 50, 'sex': 1, 'cp': 0, 'trestbps': 120, 'chol': 200, 'fbs': 0,
        'restecg': 0, 'thalach': 150, 'exang': 0, 'oldpeak': 1.0, 'slope': 1, 'ca': 0, 'thal': 2
    },
    'parkinsons': {
        'fo': 150.0, 'fhi': 200.0, 'flo': 100.0, 'jitter_percent': 0.005,
        'jitter_abs': 0.00003, 'rap': 0.01, 'ppq': 0.005, 'ddp': 0.009,
        'shimmer': 0.03, 'shimmer_db': 0.3, 'apq3': 0.025, 'apq5': 0.017,
        'apq': 0.02, 'dda': 0.02, 'nhr': 0.02, 'hnr': 0.03, 'rpde': 0.03,
        'dfa': 0.02, 'spread1': 0.02, 'spread2': 0.02, 'd2': 0.02, 'ppe': 0.02
    }
}

# Check authentication
if not st.session_state.authenticated:
    show_login_page()
else:
    # Theme toggle button (fixed position top-right)
    theme_icon = "☀️" if st.session_state.dark_mode else "🌙"
    theme_label = "Light Mode" if st.session_state.dark_mode else "Dark Mode"

    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button(theme_icon, key="theme_toggle", help=f"Switch to {theme_label}"):
            toggle_dark_mode()
            st.rerun()

    # Sidebar navigation
    display_logo()

    st.sidebar.markdown("---")

    # API Configuration
    st.sidebar.markdown("### API Configuration")
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key for AI-powered insights",
        value=st.session_state.openai_api_key,
        placeholder="sk-...",
        key="api_key_input"
    )

    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        st.sidebar.success("API Key configured")
    else:
        st.sidebar.info("Add API key for AI insights")

    st.sidebar.markdown("---")

    # Navigation menu
    selected = option_menu(
        None,
        ['Welcome', 'Diabetes', 'Heart Disease', 'Parkinsons', 'Health Planner'],
        icons=['house-fill', 'droplet-fill', 'heart-pulse-fill', 'activity', 'clipboard2-pulse-fill'],
        menu_icon=None,
        default_index=0,
        styles={
            "container": {"padding": "0"},
            "icon": {"color": "#6366f1", "font-size": "1.125rem"},
            "nav-link": {"font-size": "0.9375rem", "text-align": "left", "margin": "0.25rem 0", "border-radius": "8px", "padding": "0.75rem 1rem"},
            "nav-link-selected": {"background": "linear-gradient(135deg, #6366f1, #8b5cf6)", "color": "white"},
        },
        key="main_menu"
    )

    st.sidebar.markdown("---")

    # Logout button
    if st.sidebar.button("Sign Out", key="logout_button"):
        st.session_state.authenticated = False
        st.session_state.openai_api_key = ''
        st.rerun()

    # Welcome Page
    if selected == 'Welcome':
        show_welcome_page()

    # Diabetes Prediction Page
    elif selected == 'Diabetes':
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown("# Diabetes Risk Assessment")
        st.markdown("Machine learning-based analysis for diabetes prediction")
        st.markdown("---")

        defaults = NORMAL_DEFAULTS['diabetes']

        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = professional_input_field(
                'Pregnancies', 0, 17, defaults['pregnancies'],
                'diabetes_pregnancies',
                'Number of times pregnant (0 for never pregnant)'
            )

            SkinThickness = professional_input_field(
                'Skin Thickness', 0, 99, defaults['skin_thickness'],
                'diabetes_skin',
                'Triceps skin fold thickness (normal: 12-23mm)', 'mm'
            )

            DiabetesPedigreeFunction = professional_input_field(
                'Diabetes Pedigree Function', 0.0, 2.42, defaults['pedigree'],
                'diabetes_pedigree',
                'Genetic predisposition score (higher = more family history)'
            )

        with col2:
            Glucose = professional_input_field(
                'Glucose Level', 0, 199, defaults['glucose'],
                'diabetes_glucose',
                'Plasma glucose after 2hr oral glucose tolerance test (normal: <140)', 'mg/dL'
            )

            Insulin = professional_input_field(
                'Insulin Level', 0, 846, defaults['insulin'],
                'diabetes_insulin',
                '2-Hour serum insulin level (normal: 16-166)', 'mu U/ml'
            )

            Age = professional_input_field(
                'Age', 21, 81, defaults['age'],
                'diabetes_age',
                'Age in years (diabetes risk increases with age)', 'years'
            )

        with col3:
            BloodPressure = professional_input_field(
                'Blood Pressure', 0, 122, defaults['blood_pressure'],
                'diabetes_bp',
                'Diastolic blood pressure (normal: <80)', 'mmHg'
            )

            BMI = professional_input_field(
                'BMI', 0.0, 67.1, defaults['bmi'],
                'diabetes_bmi',
                'Body Mass Index (normal: 18.5-24.9, overweight: 25-29.9)', 'kg/m²'
            )

        st.markdown("---")

        if st.button('Analyze Diabetes Risk', key="diabetes_test_button"):
            start_time_total = time.perf_counter()

            with st.spinner("Processing analysis..."):
                start_prediction = time.perf_counter()
                user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                diab_prediction = diabetes_model.predict([user_input])
                end_prediction = time.perf_counter()
                prediction_latency = (end_prediction - start_prediction) * 1000

                diab_diagnosis = 'High diabetes risk detected' if diab_prediction[0] == 1 else 'Low diabetes risk'

                if diab_prediction[0] == 1:
                    st.error(f"Assessment Result: {diab_diagnosis}")
                else:
                    st.success(f"Assessment Result: {diab_diagnosis}")

                PerformanceMonitor.display_latency(prediction_latency, "Model Prediction")

                if st.session_state.openai_api_key:
                    with st.spinner("Generating AI analysis..."):
                        start_ai = time.perf_counter()
                        prompt = f"""
                        Based on these diabetes risk factors:
                        - Pregnancies: {Pregnancies}
                        - Glucose: {Glucose} mg/dL
                        - Blood Pressure: {BloodPressure} mmHg
                        - Skin Thickness: {SkinThickness} mm
                        - Insulin: {Insulin} mu U/ml
                        - BMI: {BMI} kg/m²
                        - Diabetes Pedigree Function: {DiabetesPedigreeFunction}
                        - Age: {Age} years

                        The prediction is: {diab_diagnosis}

                        Provide a professional explanation of the key risk factors and actionable health recommendations in 3 concise paragraphs.
                        """
                        response = generate_openai_response(prompt, st.session_state.openai_api_key)
                        end_ai = time.perf_counter()
                        ai_latency = (end_ai - start_ai) * 1000

                        st.info(f"**AI Analysis:** {response}")
                        PerformanceMonitor.display_latency(ai_latency, "AI Analysis")

                end_time_total = time.perf_counter()
                total_latency = (end_time_total - start_time_total) * 1000
                PerformanceMonitor.display_latency(total_latency, "Total Operation")

        st.markdown('</div>', unsafe_allow_html=True)

    # Heart Disease Prediction Page
    elif selected == 'Heart Disease':
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown("# Cardiovascular Risk Assessment")
        st.markdown("Comprehensive heart health analysis using advanced algorithms")
        st.markdown("---")

        defaults = NORMAL_DEFAULTS['heart']

        col1, col2, col3 = st.columns(3)
        with col1:
            age = professional_input_field(
                'Age', 29, 77, defaults['age'], 'heart_age',
                'Age in years (heart disease risk increases with age)', 'years'
            )

            trestbps = professional_input_field(
                'Resting Blood Pressure', 94, 200, defaults['trestbps'], 'heart_trestbps',
                'Resting blood pressure (normal: <120)', 'mmHg'
            )

            restecg = professional_input_field(
                'Resting ECG', 0, 2, defaults['restecg'], 'heart_restecg',
                'Resting ECG results (0=normal, 1=ST-T abnormality, 2=LV hypertrophy)'
            )

            oldpeak = professional_input_field(
                'ST Depression', 0.0, 6.2, defaults['oldpeak'], 'heart_oldpeak',
                'ST depression induced by exercise relative to rest'
            )

        with col2:
            sex = professional_input_field(
                'Sex', 0, 1, defaults['sex'], 'heart_sex',
                'Biological sex (0 = Female, 1 = Male)'
            )

            chol = professional_input_field(
                'Cholesterol', 126, 564, defaults['chol'], 'heart_chol',
                'Serum cholesterol (normal: <200)', 'mg/dl'
            )

            thalach = professional_input_field(
                'Max Heart Rate', 71, 202, defaults['thalach'], 'heart_thalach',
                'Maximum heart rate achieved during exercise', 'bpm'
            )

            slope = professional_input_field(
                'ST Slope', 0, 2, defaults['slope'], 'heart_slope',
                'Slope of peak exercise ST segment (0=down, 1=flat, 2=up)'
            )

        with col3:
            cp = professional_input_field(
                'Chest Pain Type', 0, 3, defaults['cp'], 'heart_cp',
                'Chest pain type (0=typical angina, 1=atypical, 2=non-anginal, 3=asymptomatic)'
            )

            fbs = professional_input_field(
                'Fasting Blood Sugar', 0, 1, defaults['fbs'], 'heart_fbs',
                'Fasting blood sugar > 120 mg/dl (0=false, 1=true)'
            )

            exang = professional_input_field(
                'Exercise Angina', 0, 1, defaults['exang'], 'heart_exang',
                'Exercise induced angina (0=no, 1=yes)'
            )

            ca = professional_input_field(
                'Major Vessels', 0, 4, defaults['ca'], 'heart_ca',
                'Number of major vessels colored by fluoroscopy (0-4)'
            )

        col1, col2, col3 = st.columns(3)
        with col1:
            thal = professional_input_field(
                'Thalassemia', 0, 3, defaults['thal'], 'heart_thal',
                'Thalassemia type (0=normal, 1=fixed defect, 2=reversible defect)'
            )

        st.markdown("---")

        if st.button('Analyze Heart Disease Risk', key="heart_test_button"):
            start_time_total = time.perf_counter()

            with st.spinner("Processing analysis..."):
                start_prediction = time.perf_counter()
                user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                heart_prediction = heart_disease_model.predict([user_input])
                end_prediction = time.perf_counter()
                prediction_latency = (end_prediction - start_prediction) * 1000

                heart_diagnosis = 'High cardiovascular risk detected' if heart_prediction[0] == 1 else 'Low cardiovascular risk'

                if heart_prediction[0] == 1:
                    st.error(f"Assessment Result: {heart_diagnosis}")
                else:
                    st.success(f"Assessment Result: {heart_diagnosis}")

                PerformanceMonitor.display_latency(prediction_latency, "Model Prediction")

                if st.session_state.openai_api_key:
                    with st.spinner("Generating AI analysis..."):
                        start_ai = time.perf_counter()
                        prompt = f"""
                        Based on these cardiovascular risk factors:
                        - Age: {age} years, Sex: {'Male' if sex == 1 else 'Female'}
                        - Chest Pain Type: {cp}, Blood Pressure: {trestbps} mmHg
                        - Cholesterol: {chol} mg/dl, Fasting Blood Sugar: {'High' if fbs == 1 else 'Normal'}
                        - Max Heart Rate: {thalach} bpm, Exercise Angina: {'Yes' if exang == 1 else 'No'}
                        - ST Depression: {oldpeak}, Major Vessels: {ca}

                        The prediction is: {heart_diagnosis}

                        Provide a professional explanation of the key risk factors and actionable cardiovascular health recommendations in 3 concise paragraphs.
                        """
                        response = generate_openai_response(prompt, st.session_state.openai_api_key)
                        end_ai = time.perf_counter()
                        ai_latency = (end_ai - start_ai) * 1000

                        st.info(f"**AI Analysis:** {response}")
                        PerformanceMonitor.display_latency(ai_latency, "AI Analysis")

                end_time_total = time.perf_counter()
                total_latency = (end_time_total - start_time_total) * 1000
                PerformanceMonitor.display_latency(total_latency, "Total Operation")

        st.markdown('</div>', unsafe_allow_html=True)

    # Parkinson's Prediction Page
    elif selected == "Parkinsons":
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown("# Parkinson's Disease Assessment")
        st.markdown("Advanced voice analysis for neurological health screening")
        st.markdown("---")

        defaults = NORMAL_DEFAULTS['parkinsons']

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = professional_input_field('MDVP:Fo(Hz)', 88.33, 260.10, defaults['fo'], 'parkinsons_fo',
                                         'Average vocal fundamental frequency', 'Hz')
            RAP = professional_input_field('MDVP:RAP', 0.0068, 0.02144, defaults['rap'], 'parkinsons_rap',
                                          'Relative average perturbation')
            Shimmer = professional_input_field('MDVP:Shimmer', 0.019, 0.119, defaults['shimmer'], 'parkinsons_shimmer',
                                              'Local shimmer variation')
            APQ = professional_input_field('MDVP:APQ', 0.0165, 0.0378, defaults['apq'], 'parkinsons_apq',
                                          'Amplitude perturbation quotient')
            RPDE = professional_input_field('RPDE', 0.0165, 0.0378, defaults['rpde'], 'parkinsons_rpde',
                                           'Recurrence period density entropy')

        with col2:
            fhi = professional_input_field('MDVP:Fhi(Hz)', 102.14, 592.03, defaults['fhi'], 'parkinsons_fhi',
                                          'Maximum vocal fundamental frequency', 'Hz')
            PPQ = professional_input_field('MDVP:PPQ', 0.003446, 0.01958, defaults['ppq'], 'parkinsons_ppq',
                                          'Period perturbation quotient')
            Shimmer_dB = professional_input_field('MDVP:Shimmer(dB)', 0.165, 0.378, defaults['shimmer_db'], 'parkinsons_shimmer_db',
                                                 'Local shimmer in dB')
            DDA = professional_input_field('Shimmer:DDA', 0.0165, 0.0378, defaults['dda'], 'parkinsons_dda',
                                          'Average absolute difference of differences')
            DFA = professional_input_field('DFA', 0.0165, 0.0378, defaults['dfa'], 'parkinsons_dfa',
                                          'Detrended fluctuation analysis')

        with col3:
            flo = professional_input_field('MDVP:Flo(Hz)', 65.47, 239.17, defaults['flo'], 'parkinsons_flo',
                                          'Minimum vocal fundamental frequency', 'Hz')
            DDP = professional_input_field('Jitter:DDP', 0.00204, 0.06433, defaults['ddp'], 'parkinsons_ddp',
                                          'Average absolute difference of differences')
            APQ3 = professional_input_field('Shimmer:APQ3', 0.0165, 0.0378, defaults['apq3'], 'parkinsons_apq3',
                                           '3-point amplitude perturbation quotient')
            NHR = professional_input_field('NHR', 0.0165, 0.0378, defaults['nhr'], 'parkinsons_nhr',
                                          'Noise-to-harmonics ratio')
            spread1 = professional_input_field('spread1', 0.0165, 0.0378, defaults['spread1'], 'parkinsons_spread1',
                                              'Nonlinear dynamical complexity measure')

        with col4:
            Jitter_percent = professional_input_field('MDVP:Jitter(%)', 0.00168, 0.03316, defaults['jitter_percent'], 'parkinsons_jitter_percent',
                                                     'Jitter as a percentage')
            APQ5 = professional_input_field('Shimmer:APQ5', 0.0165, 0.0378, defaults['apq5'], 'parkinsons_apq5',
                                           '5-point amplitude perturbation quotient')
            HNR = professional_input_field('HNR', 0.0165, 0.0378, defaults['hnr'], 'parkinsons_hnr',
                                          'Harmonics-to-noise ratio')
            spread2 = professional_input_field('spread2', 0.0165, 0.0378, defaults['spread2'], 'parkinsons_spread2',
                                              'Nonlinear dynamical complexity measure')

        with col5:
            Jitter_Abs = professional_input_field('MDVP:Jitter(Abs)', 0.000007, 0.00261, defaults['jitter_abs'], 'parkinsons_jitter_abs',
                                                 'Absolute jitter in seconds')
            D2 = professional_input_field('D2', 0.0165, 0.0378, defaults['d2'], 'parkinsons_d2',
                                         'Correlation dimension')
            PPE = professional_input_field('PPE', 0.0165, 0.0378, defaults['ppe'], 'parkinsons_ppe',
                                          'Pitch period entropy')

        st.markdown("---")

        if st.button("Analyze Parkinson's Risk", key="parkinsons_test_button"):
            start_time_total = time.perf_counter()

            with st.spinner("Processing analysis..."):
                start_prediction = time.perf_counter()
                user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                             APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
                parkinsons_prediction = parkinsons_model.predict([user_input])
                end_prediction = time.perf_counter()
                prediction_latency = (end_prediction - start_prediction) * 1000

                parkinsons_diagnosis = "Parkinson's indicators detected" if parkinsons_prediction[0] == 1 else "No Parkinson's indicators detected"

                if parkinsons_prediction[0] == 1:
                    st.error(f"Assessment Result: {parkinsons_diagnosis}")
                else:
                    st.success(f"Assessment Result: {parkinsons_diagnosis}")

                PerformanceMonitor.display_latency(prediction_latency, "Model Prediction")

                if st.session_state.openai_api_key:
                    with st.spinner("Generating AI analysis..."):
                        start_ai = time.perf_counter()
                        prompt = f"""
                        Based on voice analysis parameters for Parkinson's disease screening:
                        - Fundamental frequency measures: Fo={fo}Hz, Fhi={fhi}Hz, Flo={flo}Hz
                        - Jitter measures: {Jitter_percent}%, Abs={Jitter_Abs}s
                        - Shimmer measures: {Shimmer}, {Shimmer_dB}dB
                        - Noise ratios: NHR={NHR}, HNR={HNR}

                        The prediction is: {parkinsons_diagnosis}

                        Provide a professional explanation of the voice analysis results and recommendations for neurological health in 3 concise paragraphs.
                        """
                        response = generate_openai_response(prompt, st.session_state.openai_api_key)
                        end_ai = time.perf_counter()
                        ai_latency = (end_ai - start_ai) * 1000

                        st.info(f"**AI Analysis:** {response}")
                        PerformanceMonitor.display_latency(ai_latency, "AI Analysis")

                end_time_total = time.perf_counter()
                total_latency = (end_time_total - start_time_total) * 1000
                PerformanceMonitor.display_latency(total_latency, "Total Operation")

        st.markdown('</div>', unsafe_allow_html=True)

    # Personalized Health Plan Page
    elif selected == "Health Planner":
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown("# Personalized Health & Fitness Planner")
        st.markdown("AI-powered personalized health recommendations")
        st.markdown("---")

        if 'dietary_plan' not in st.session_state:
            st.session_state.dietary_plan = {}
            st.session_state.fitness_plan = {}
            st.session_state.plans_generated = False

        st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(139, 92, 246, 0.08));
                        padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border: 1px solid rgba(99, 102, 241, 0.15);'>
                <p style='font-size: 1.0625rem; font-weight: 500; margin: 0; text-align: center; color: #475569;'>
                Get personalized dietary and fitness plans tailored to your goals and preferences.
                Our AI-powered system considers your unique profile to create the optimal plan for you.
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.session_state.openai_api_key:
            st.markdown("### Your Health Profile")
            col1, col2 = st.columns(2)

            with col1:
                age = professional_input_field("Age", 10, 100, 50, "profile_age",
                                             "Your current age affects metabolism and nutritional needs", "years")
                height = professional_input_field("Height", 100.0, 250.0, 175.0, "profile_height",
                                                "Height in centimeters for BMI calculation", "cm")
                activity_level = st.selectbox(
                    "Activity Level",
                    options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"],
                    index=2,
                    help="Choose your typical weekly activity level"
                )
                dietary_preferences = st.selectbox(
                    "Dietary Preferences",
                    options=["Balanced", "Vegetarian", "Keto", "Gluten Free", "Low Carb", "Dairy Free"],
                    help="Select your preferred dietary approach"
                )

            with col2:
                weight = professional_input_field("Weight", 20.0, 300.0, 70.0, "profile_weight",
                                                "Current weight for calculating nutritional needs", "kg")
                sex = st.selectbox("Sex", options=["Male", "Female", "Other"], index=0)
                fitness_goals = st.selectbox(
                    "Fitness Goals",
                    options=["Lose Weight", "Gain Muscle", "Endurance", "Stay Fit", "Strength Training"],
                    index=3,
                    help="What do you want to achieve?"
                )

            st.markdown("---")

            if st.button("Generate Personalized Plan", key="generate_plan_button"):
                start_time_total = time.perf_counter()

                with st.spinner("Creating your personalized health routine..."):
                    try:
                        bmi = weight / ((height/100) ** 2)
                        bmi_category = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"

                        user_profile = f"""
                        Age: {age} years
                        Weight: {weight}kg
                        Height: {height}cm
                        BMI: {bmi:.1f} ({bmi_category})
                        Sex: {sex}
                        Activity Level: {activity_level}
                        Dietary Preferences: {dietary_preferences}
                        Fitness Goals: {fitness_goals}
                        """

                        start_ai = time.perf_counter()

                        dietary_prompt = f"""
                        Create a personalized daily meal plan for:
                        {user_profile}

                        Include:
                        - Specific meals (breakfast, lunch, dinner, 2 snacks)
                        - Portion sizes and calories
                        - Why this plan works for their goals
                        - Important nutritional considerations

                        Format as structured recommendations.
                        """

                        fitness_prompt = f"""
                        Design a personalized weekly fitness routine for:
                        {user_profile}

                        Include:
                        - Specific exercises with sets/reps/duration
                        - Weekly schedule (which days for which activities)
                        - Progression plan
                        - Recovery recommendations
                        - Safety tips and modifications

                        Format as a structured weekly plan.
                        """

                        dietary_response = generate_openai_response(dietary_prompt, st.session_state.openai_api_key)
                        fitness_response = generate_openai_response(fitness_prompt, st.session_state.openai_api_key)

                        end_ai = time.perf_counter()
                        ai_latency = (end_ai - start_ai) * 1000

                        st.success(f"Plans generated successfully. Your BMI: {bmi:.1f} ({bmi_category})")

                        st.markdown("### Dietary Plan")
                        st.info(dietary_response)

                        st.markdown("### Fitness Plan")
                        st.info(fitness_response)

                        PerformanceMonitor.display_latency(ai_latency, "AI Plan Generation")

                        end_time_total = time.perf_counter()
                        total_latency = (end_time_total - start_time_total) * 1000
                        PerformanceMonitor.display_latency(total_latency, "Total Operation")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your OpenAI API key in the sidebar to generate personalized plans.")

        st.markdown('</div>', unsafe_allow_html=True)

# Professional footer
st.markdown(
    """
    <div class="app-footer">
        <span>AI Health Copilot Pro | Agentic AI Masterclass Project</span>
        <span style="margin: 0 1rem;">•</span>
        <span>Copyright © 2026 Harry Patria - Patria & Co.</span>
        <span style="margin: 0 1rem;">•</span>
        <span>All Rights Reserved</span>
    </div>
    """,
    unsafe_allow_html=True
)
