import streamlit as st
from planner import generate_trip

st.set_page_config(page_title="Trip Planner", page_icon="🌍")
st.title("🗺️ Planificateur de voyage")

question = st.text_input("Pose ta question voyage ici (ex : programme 3 jours à Rome)")

if st.button("Envoyer"):
    if question.strip() == "":
        st.warning("Merci d'entrer une question.")
    else:
        with st.spinner("🤖 Génération en cours..."):
            answer = generate_trip(question)
            st.markdown(f"**Chatbot :** {answer}")
