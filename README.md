
# 🌙 Dream Journal Visualizer (AI-Powered)

Turn your dreams into stunning AI-generated visuals!  
This Streamlit-based app lets you submit a dream description and generates a dream-inspired image using Stable Diffusion.

---

## ✨ Features

- 📝 Submit dream title, mood, date, and description
- 🎨 Generates beautiful images using Stable Diffusion v1.5
- 🌈 Mood selection and intuitive input form
- 🧠 Recent dreams gallery (sidebar preview)
- 💾 Saves each dream image with a unique name
- 🎯 Fast local image generation (GPU-powered)
- 💻 Clean, responsive, and modern dashboard UI

---

## 🚀 Technologies Used

- [Streamlit](https://streamlit.io/) — Web UI
- [Diffusers by Hugging Face](https://huggingface.co/docs/diffusers/index) — Stable Diffusion
- [Torch (PyTorch)](https://pytorch.org/) — Model backend
- [PIL / Pillow](https://python-pillow.org/) — Image saving
- PostgreSQL (optional) — for storing dream records

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dream-journal-ai.git
cd dream-journal-ai
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary>📌 Example <code>requirements.txt</code></summary>

```
torch
transformers
diffusers
Pillow
streamlit
```
</details>

### 4. Authenticate with Hugging Face

- Sign in to [Hugging Face](https://huggingface.co)
- Accept the license for [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- Run:

```bash
huggingface-cli login
```

- Paste your token.

### 5. Run the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Example Prompts

Try pasting these dream descriptions in the app:

**➤ “Flying Through a Neon City”**

_I was flying over a futuristic city filled with neon lights and floating cars. The sky was purple, and everything felt calm and surreal._

**➤ “Forest of Whispers”**

_I walked through a glowing forest where the trees whispered ancient secrets. There were mushrooms lighting my path._

---

## 📁 Folder Structure

```
dream_journal/
├── app.py              # Main Streamlit app
├── image_gen.py        # Stable Diffusion pipeline
├── images/             # Saved dream images
├── venv/               # Virtual environment
├── README.md
└── requirements.txt
```

---

## 💡 Future Ideas

- 🧠 NLP analysis (keywords, sentiment)
- 🌐 Interactive dream network map (NetworkX + PyVis)
- 🗃 Save dreams to PostgreSQL
- 🧑‍🤝‍🧑 Community dream sharing
- 📥 Download/share button

---

## 🙌 Author

**Balu K**  
B.Tech AI & DS @ Karunya Institute of Technology and Sciences  
Frontend & Flutter Developer | Passionate about AI-powered apps
