import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import base64
import os

# --- 1. وظيفة الخلفية المضمونة للسيرفر ---
def set_bg_from_local():
    img_name = 'lab.JPG' # سيبحث عن الصورة المرفوعة بجانبه في GitHub
    if os.path.exists(img_name):
        with open(img_name, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        style = f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 45, 93, 0.65), rgba(0, 45, 93, 0.65)), url("data:image/png;base64,{b64_encoded}");
            background-size: cover; background-attachment: fixed;
        }}
        .main-card {{
            background-color: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px); padding: 40px; border-radius: 30px; 
            border: 1px solid rgba(255, 255, 255, 0.3); margin: auto; max-width: 1000px;
        }}
        h1, h2, h3, p, span, label, .stMarkdown {{ 
            color: #ffffff !important; text-shadow: 2px 2px 8px rgba(0,0,0,0.8); font-family: 'Segoe UI', sans-serif;
        }}
        .stSlider [data-baseweb="slider"] div div {{ background-color: #ff4b4b !important; }}
        .stSlider [role="slider"] {{ background-color: #ff4b4b !important; border: 2px solid white; }}
        .stButton>button {{ 
            background: #ffffff; color: #001a33 !important; border-radius: 15px; height: 60px; width: 100%; 
            font-weight: 900; border: none; font-size: 20px; 
        }}
        </style>
        """
        st.markdown(style, unsafe_allow_html=True)
        return True
    return False

st.set_page_config(page_title="Elite AI Suite", page_icon="🧬", layout="wide")
set_bg_from_local()

@st.cache_resource
def load_ai():
    data = load_breast_cancer()
    idx = [0, 1, 2, 3, 4, 5, 6, 7]
    X = pd.DataFrame(data.data[:, idx], columns=[data.feature_names[i] for i in idx])
    model = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, data.target)
    return model, [data.feature_names[i] for i in idx]

model, features = load_ai()

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 3.5em;'>🧬 CLINICAL INTELLIGENCE PRO</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1.5])
with col1:
    st.markdown("<h1 style='font-size: 180px; text-align: center; margin: 0;'>🔬</h1>", unsafe_allow_html=True)
    st.success("📡 AI Status: Live")
with col2:
    st.subheader("📋 Laboratory Parameters")
    inputs = []
    c1, c2 = st.columns(2)
    for i, name in enumerate(features):
        with c1 if i % 2 == 0 else c2:
            val = st.slider(name.replace('mean ', '').capitalize(), 5.0, 40.0, 18.0, key=f"s_{i}")
            inputs.append(val)

st.write("---")
if st.button("🚀 EXECUTE CLINICAL DIAGNOSTIC SCAN"):
    pred = model.predict([inputs])
    prob = model.predict_proba([inputs])[0][pred[0]] * 100
    if pred == 0:
        st.error(f"🚨 ALERT: High Risk Detected ({float(prob):.1f}%)")
    else:
        st.success(f"✅ NORMAL: Healthy Pattern Identified ({float(prob):.1f}%)")
        st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

