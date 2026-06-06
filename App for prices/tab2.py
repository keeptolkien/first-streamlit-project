import streamlit as st

def count_words(text):
    return len(text.split())

def tab_count_words():
    text = st.text_area('Введите текст: ')

    count_button = st.button('Посчитать')

    if count_button:
        if text:
            result = count_words(text)
            st.write(f'Количество слов: {result}')
        else:
            st.warning('Не введен текст')
            

