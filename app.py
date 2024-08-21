# app.py
import streamlit as st
from src.chatbot import responder_pergunta

st.title("Chatbot Vestibular Unicamp 2024")
pergunta = st.text_input("Digite sua pergunta:")
if pergunta:
    with open("data/edital.txt", "r", encoding="utf-8") as f:
        edital_text = f.read()
    resposta = responder_pergunta(pergunta, edital_text)
    st.write(resposta)
