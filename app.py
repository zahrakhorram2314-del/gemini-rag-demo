import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini RAG App", page_icon="🤖", layout="wide")

st.title("Gemini AI Smart Assistant")
st.write("Google Developers Competition Evaluation and Judging Project")

api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if not api_key:
    st.info("Please enter your API key in the sidebar to activate the application.", icon="🔑")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your question or request..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})


