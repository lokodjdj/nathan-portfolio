
import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Nathan's Portfolio", layout="centered")

# Avatar or Logo
st.image("https://i.imgur.com/7XqfG7M.png", width=120)  # Replace with your own image URL

# Main Title
st.title("🎓 Nathan Abikzir")
st.subheader("8th Grade | Inventure Academy")

# Introduction
st.write("👋 Hi! I'm **Nathan**, a creative and tech-savvy 13-year-old who loves to build, explore, and try new things. This is my interactive portfolio!")

# Skills Section
st.markdown("### 💡 Top Skills")
skills = ["🎨 Creativity", "💻 Tech", "🤝 Teamwork"]
st.write(", ".join(skills))

# Project Highlight
st.markdown("### 🚀 Project I'm Proud Of")
st.info("🕰️ **History Project** – I explored fascinating historical events and figures, researched deeply, and presented my work in a creative and engaging way.")

# Activities & Clubs
st.markdown("### 🎸 Clubs & Activities")
st.write("- Played for **Sudden Blues** basketball")
st.write("- Participated in school group projects and team events")

# Interests
st.markdown("### 🎮 Hobbies & Interests")
interests = [
    "🎵 Playing basket ball", "🧪 Tech experiments", "🎮 Gaming", 
    "🎨 Digital art", "📽️ Animation", "💬 Storytelling"
]
for i in interests:
    st.write(f"- {i}")

# Learning Goals
st.markdown("### 🔭 Things I'm Excited to Learn")
goals = [
    "🚀 Building apps & games", 
    "🎥 Video editing & animations", 
    "🤖 AI and how it works", 
    "🖼️ Creating digital art", 
    "🎤 Public speaking"
]
for g in goals:
    st.write(f"- {g}")

# Footer / Contact
st.markdown("---")
st.write("📫 Want to connect or see more? [Send me a message](mailto:lokodjdj81@gmail.com)")

# Optional: Custom background or theme
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    </style>
    """, unsafe_allow_html=True
)
