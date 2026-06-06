import streamlit as st
from test_divisors import find_divisors

def file_uploader():
    uploaded_file = st.file_uploader("Загрузите файл в формате txt: ", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8")

        result = ''
        for i in text.split():
            num = int(i)
            divs = find_divisors(num)
            result += f'- **{num}**: *{', '.join(divs)}*\n\n'

        st.markdown(result)


