import streamlit as st
from string_analyzer import find_sequence

st.title('Анализатор последовательности')

# st.header('Sequence analyzer')

text = st.text_input('Введите текст: ')
string_button = st.button('Найти последовательность')

mode = st.radio(
    "Где искать последовательности?",
    ("Во всех символах", "Только в буквах", "Только в цифрах")
)

if string_button:
    if text:
        result = find_sequence(text, mode)
        if result:
            for symbol, count, sequence in result:
                st.write("---")
                st.write(f"**Символ:** {symbol}")
                st.write(f"**Длина:** {count}")
                st.write(f"**Последовательность:** {sequence}")

        else:
            st.info("Последовательностей нет.")
    else:
        st.warning('Не введен текст')