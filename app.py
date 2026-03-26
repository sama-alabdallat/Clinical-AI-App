def set_bg_from_local():
    # كود ذكي بيبحث عن الصورة بأي اسم (كبير أو صغير)
    img_name = ""
    for file in os.listdir():
        if file.lower() == "lab.jpg":
            img_name = file
            break
            
    if img_name:
        with open(img_name, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        style = f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 45, 93, 0.7), rgba(0, 45, 93, 0.7)), url("data:image/png;base64,{b64_encoded}");
            background-size: cover; background-attachment: fixed;
        }}
        .main-card {{
            background-color: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px); padding: 40px; border-radius: 30px; 
            border: 1px solid rgba(255, 255, 255, 0.3); margin: auto; max-width: 1100px;
        }}
        /* إجبار الخطوط تكون بيضاء فخمة */
        h1, h2, h3, p, span, label, .stMarkdown, .css-10trblm {{ 
            color: #ffffff !important; text-shadow: 2px 2px 8px rgba(0,0,0,0.8) !important;
        }}
        .stSlider [data-baseweb="slider"] div div {{ background-color: #ff4b4b !important; }}
        .stButton>button {{ background: #ffffff; color: #001a33 !important; font-weight: 900; }}
        </style>
        """
        st.markdown(style, unsafe_allow_html=True)
