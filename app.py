# app.py

import streamlit as st
from image_gen import generate_image
import uuid
import os
import datetime

# Custom page config
st.set_page_config(
    page_title="Dream Journal Visualizer",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern dark theme UI
st.markdown("""
    <style>
    body, .stApp {
        background: #181c24 !important;
        color: #e6e6e6 !important;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #8ab4f8;
        margin-bottom: 1rem;
        letter-spacing: 1px;
    }
    .dream-card {
        background: #23283a;
        border-radius: 18px;
        box-shadow: 0 2px 16px #000a2a99;
        border: 1px solid #27314a;
        padding: 1.5rem 1.5rem;
        margin-bottom: 1.5rem;
        transition: box-shadow 0.2s;
        min-width: 270px;
        max-width: 370px;
        color: #e6e6e6;
    }
    .dream-card h1, .dream-card h2, .dream-card h3, .dream-card h4, .dream-card h5, .dream-card h6,
    .dream-card .card-title, .dream-card .dream-card-title, .dream-card .dream-header,
    .dream-header, .sidebar-title {
        color: #fff !important;
        font-weight: bold !important;
    }
    .dream-card:hover {
        box-shadow: 0 6px 24px #8ab4f844;
    }
    .dream-form label, .dream-form > div > label, .dream-form label span, .dream-form label[data-testid="stWidgetLabel"], .dream-form label span, .dream-form label div, .dream-form label[aria-label], .dream-form label > div {
        color: #fff !important;
        font-weight: bold !important;
        text-shadow: none !important;
    }
    .custom-label {
        color: #fff !important;
        font-weight: bold !important;
        margin-bottom: 0.2rem;
        display: block;
    }
    .dream-form textarea, .dream-form input, .dream-form select {
        color: #e6e6e6 !important;
        background: #23283a !important;
        border-radius: 8px !important;
        border: 1px solid #35405c !important;
    }
    .dream-form textarea {
        min-height: 120px;
    }
    .dream-form input[type="date"] {
        color-scheme: dark;
    }
    .dream-form .stButton > button {
        background: linear-gradient(90deg, #5f72bd 0%, #9a5cff 100%);
        color: #fff;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 2px 8px #5f72bd33;
        transition: background 0.2s;
    }
    .dream-form .stButton > button:hover {
        background: linear-gradient(90deg, #9a5cff 0%, #5f72bd 100%);
    }
    .sidebar-title {
        font-size: 26px;
        font-weight: bold;
        color: #8ab4f8;
        padding-top: 1rem;
        text-shadow: none;
    }
    .dream-footer {
        text-align: center;
        color: #b2b8d8;
        font-size: 1.1rem;
        margin-top: 2rem;
        letter-spacing: 1px;
    }
    .dream-header {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        color: #8ab4f8;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
        text-shadow: 0 2px 24px #5f72bd44;
    }
    .dream-subheader {
        text-align: center;
        font-size: 1.05rem;
        color: #b2b8d8;
        margin-bottom: 2rem;
    }
    .stImage > img {
        border-radius: 12px;
        box-shadow: 0 2px 12px #8ab4f822;
        margin-top: 0.5rem;
        border: 1px solid #27314a;
    .dream-form textarea {
        min-height: 120px;
    }
    .dream-form input[type="date"] {
        color-scheme: dark;
    }
    .dream-form .stButton > button {
        background: linear-gradient(90deg, #6a82fb 0%, #fc5c7d 100%);
        color: white;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 2px 8px #6a82fb33;
        transition: background 0.2s;
    }
    .dream-form .stButton > button:hover {
        background: linear-gradient(90deg, #fc5c7d 0%, #6a82fb 100%);
    }
    .sidebar-title {
        font-size: 26px;
        font-weight: bold;
        color: #ffe082;
        padding-top: 1rem;
        text-shadow: 0 2px 12px #fc5c7d88;
    }
    .dream-footer {
        text-align: center;
        color: #b2b8d8;
        font-size: 1.1rem;
        margin-top: 2rem;
        letter-spacing: 1px;
    }
    .dream-header {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffe082;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 24px #6a82fb88;
        letter-spacing: 2px;
    }
    .dream-subheader {
        text-align: center;
        font-size: 1.3rem;
        color: #e0e6f7;
        margin-bottom: 2.5rem;
        text-shadow: 0 2px 12px #232526;
    }
    .stImage > img {
        border-radius: 24px;
        box-shadow: 0 4px 24px #6a82fb33;
        margin-top: 1rem;
        border: 2px solid #6a82fb33;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #232526 0%, #6a82fb 100%); border-radius: 18px; padding: 1.5rem 1rem 1rem 1rem; margin-bottom: 1.5rem; box-shadow: 0 2px 12px #6a82fb33;">
        <div class="sidebar-title">
            <span style="font-size:2rem;">🗂️</span> Dream History
        </div>
""", unsafe_allow_html=True)

if not os.path.exists("images/"):
    os.makedirs("images/")

dream_files = sorted(os.listdir("images/"), reverse=True)[:5]  # Show last 5
for file in dream_files:
    st.sidebar.image(f"images/{file}", width=100, caption=file.split('.')[0])

st.sidebar.markdown("""
        <hr style="border: 1px solid #6a82fb33;">
        <div style="text-align:center; color:#ffe082; margin-top:1rem;">
            Made with <span style="color:#fc5c7d;">❤️</span> by <b>Balu K</b>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------- Main App ----------
st.markdown('<div class="dream-header">🌌 AI Dream Visualizer</div>', unsafe_allow_html=True)
st.markdown('<div class="dream-subheader">Turn your dreams into AI-generated art ✨</div>', unsafe_allow_html=True)

# --- Dream Form ---
st.markdown('<div class="dream-card">', unsafe_allow_html=True)
with st.form("dream_form"):
    st.markdown('<div class="dream-form">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<label class="custom-label">📝 Dream Title</label>', unsafe_allow_html=True)
        title = st.text_input("", placeholder="e.g. Flying Through a Neon City", label_visibility="collapsed")
        st.markdown('<label class="custom-label">😊 Mood of the Dream</label>', unsafe_allow_html=True)
        mood = st.selectbox("", ["Peaceful", "Mysterious", "Exciting", "Scary", "Confusing", "Uplifting"], label_visibility="collapsed")
    with col2:
        st.markdown('<label class="custom-label">📅 Date of the Dream</label>', unsafe_allow_html=True)
        dream_date = st.date_input("", value=datetime.date.today(), label_visibility="collapsed")
    st.markdown('<label class="custom-label">🧠 Describe Your Dream</label>', unsafe_allow_html=True)
    description = st.text_area("", height=180, placeholder="Write about what happened in your dream...", label_visibility="collapsed")
    submitted = st.form_submit_button("🎨 Generate Image")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Image Generation Logic ---
if submitted:
    if not description.strip():
        st.warning("Please describe your dream.")
    else:
        with st.spinner("Dreaming... Creating your image... ✨"):
            unique_id = str(uuid.uuid4())[:8]
            image_path = f"images/{unique_id}.png"
            saved_path = generate_image(description, image_path)

        # --- Dream Result Card ---
        st.markdown('<div class="dream-card" style="border: 2px solid #6a82fb; box-shadow: 0 0 32px #fc5c7d66;">', unsafe_allow_html=True)
        st.success("Here is your dream visualized:")
        st.image(saved_path, use_column_width=True, caption=f"🖼️ {title or 'Untitled Dream'} ({dream_date})")
        from nlp_utils import analyze_dream
        from db import insert_dream
        keywords, sentiment = analyze_dream(description)
        st.markdown(f"""
        <div style='margin-top:1.5rem;'>
        <span style="font-size:1.2rem; color:#ffe082; font-weight:600;">✨ Title:</span> <span style="color:#e0e6f7;">{title or 'Untitled'}</span><br>
        <span style="font-size:1.2rem; color:#6a82fb; font-weight:600;">😊 Mood:</span> <span style="color:#e0e6f7;">{mood}</span><br>
        <span style="font-size:1.2rem; color:#fc5c7d; font-weight:600;">📅 Date:</span> <span style="color:#e0e6f7;">{dream_date}</span><br>
        <span style="font-size:1.2rem; color:#ffe082; font-weight:600;">🔑 Keywords:</span> <span style="color:#e0e6f7;">{keywords}</span><br>
        <span style="font-size:1.2rem; color:#6a82fb; font-weight:600;">💬 Sentiment:</span> <span style="color:#e0e6f7;">{sentiment}</span><br>
        <span style="font-size:1.2rem; color:#fc5c7d; font-weight:600;">💾 Saved As:</span> <span style="color:#b2b8d8;">{saved_path}</span>
        </div>
        """, unsafe_allow_html=True)
        # Store dream in the database with error handling
        try:
            insert_dream(
                title or "Untitled",
                dream_date,
                mood,
                description,
                saved_path,
                keywords,
                sentiment
            )
        except Exception as e:
            st.error(f"Failed to save dream to database: {e}")
            print(f"[DB ERROR] {e}")
        st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="dream-footer">
    <span style="font-size:1.2rem;">🌙</span> <i>"Dreams are illustrations... from the book your soul is writing about you."</i> <span style="font-size:1.2rem;">✨</span><br>
    <span style="font-size:0.95rem; color:#6a82fb;">Enjoy visualizing your dreams every night!</span>
</div>
""", unsafe_allow_html=True)
