from tab1 import sales_calculater
import streamlit as st
from tab2 import tab_count_words
from tab3 import file_uploader


def page1():

    st.title('Multitask App')

    tab1, tab2, tab3 = st.tabs(["Расчет скидки", "Подсчет слов", "Загрузить файл"])

    with tab1:
        sales_calculater()
    with tab2:
        tab_count_words()

    with tab3:
        file_uploader()

page1()