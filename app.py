import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import base64
import os

st.set_page_config(page_title="Clinical AI Enterprise", page_icon="🧬", layout="wide")

def apply_custom_design():
    img_name = ""
    for file in os.listdir():
        if "lab" in file.lower():
            img_name = file
            break

    bg_style = ""
    if img_name:
        with open(img_name, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        bg_style = f'background-image: linear-gradient(rgba(0, 45, 93, 0.7), rgba(0, 45, 93, 0.7)), url("data:image/png;base64,{b64}");'
    else:
        bg_style = 'background: linear-gradient(135deg, #002d5d 0%, #00509d 100%);'

    st.markdown(f"""
        <style>
        .stApp {{
            {bg_style}
            background-size: cover;
            background-attachment: fixed;
        }}
        .main-card {{
            background-color: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(15px);
            padding: 45px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin: auto;
            max-width: 1100px;
        }}
        h1, h2, h3, p, span, label, .stMarkdown {{ 
            color: #ffffff !important; 
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8) !important;
            font-family: 'Segoe UI', sans-serif;
        }}
        .stSlider [data-baseweb="slider"] div div {{ background-color: #ff4b4b !important; }}
        .stSlider [role="slider"] {{ background-color: #ff4b4b !important; border: 2px solid white; }}
        .stButton>button {{ 
            background: #ffffff; 
            color: #001a33 !important; 
            border-radius: 15px; 
            height: 65px; 
            width: 100%; 
            font-weight: 900; 
            border: none; 
            font-size: 22px; 
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
            text-transform: uppercase;
        }}
        .stButton>button:hover {{ background: #f0f0f0; transform: translateY(-2px); }}
        </style>
        """, unsafe_allow_html=True)

apply_custom_design()

@st.cache_resource
def load_ai_model():
    data = load_breast_cancer()
    idx = [0, 1, 2, 3, 4, 5, 6, 7]
    X = pd.DataFrame(data.data[:, idx], columns=[data.feature_names[i] for i in idx])
    model = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, data.target)
    return model, [data.feature_names[i] for i in idx]

model, features = load_ai_model()

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 3.5em;'>🧬 CLINICAL INTELLIGENCE PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3em;'>Professional Medical Analysis Powered by Machine Learning</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1.5])
with col1:
    st.markdown("<h1 style='font-size: 180px; text-align: center; margin: 0;'>🔬</h1>", unsafe_allow_html=True)
    st.success("📡 AI Core Status: Live")
    st.info("**Methodology:** Random Forest Neural Recognition")

with col2:
    st.subheader("📋 Laboratory Clinical Parameters")
    user_inputs = []
    c1, c2 = st.columns(2)
    for i, name in enumerate(features):
        with c1 if i % 2 == 0 else c2:
            val = st.slider(name.replace('mean ', '').capitalize(), 5.0, 40.0, 18.0, key=f"s_{i}")
            user_inputs.append(val)

st.write("---")
if st.button("🚀 EXECUTE CLINICAL DIAGNOSTIC SCAN"):
    with st.spinner('Synchronizing Data...'):
        prediction = model.predict([user_inputs])
        probabilities = model.predict_proba([user_inputs])[0]
        confidence = probabilities[prediction[0]] * 100
        
    st.subheader("Diagnostic Intelligence Report:")
    if prediction[0] == 0:
        st.error(f"🚨 ALERT: High Risk Detected (Confidence: {float(confidence):.1f}%)")
    else:
        st.success(f"✅ NORMAL: Healthy Pattern Identified (Confidence: {float(confidence):.1f}%)")
        st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; margin-top: 30px; font-weight: bold;'>Designed & Developed by Sama Alabdallat | Clinical AI Division © 2026</p>", unsafe_allow_html=True)
