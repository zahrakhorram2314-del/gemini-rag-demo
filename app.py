import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini RAG App", page_icon="🤖", layout="wide")

st.title("🤖 دستیار هوشمند مبتنی بر Gemini AI")
st.write("پروژه ارزیابی و داوری مسابقات توسعه‌دهندگان گوگل")

api_key = st.sidebar.text_input("کلید API Gemini را وارد کنید:", type="password")

if not api_key:
    st.info("لطفاً کلید API خود را در نوار کناری وارد کنید تا برنامه فعال شود.", icon="🔑")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("سوال یا درخواست خود را بنویسید..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("در حال دریافت پاسخ..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

