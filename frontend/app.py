import streamlit as st
import requests

st.title("Healthcare Clinical Note Chatbot")

question = st.text_input("Enter your medical query:")
if st.button("Submit") and question:
    with st.spinner("Fetching answer..."):
        response = requests.post(
            "http://localhost:8000/query", 
            json={"question": question}
        )
        st.write("**Answer:**", response.json().get("answer", "No answer returned."))