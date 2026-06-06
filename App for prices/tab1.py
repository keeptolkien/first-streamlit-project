from backend import calculate_price
import streamlit as st

def sales_calculater():
    start_price = st.number_input(label='Цена товара: ', min_value=0, max_value=1000)
    amount = st.number_input(label='Количество (целое число): ', min_value=1, max_value=1000, step=1)
    discount = st.number_input(label='Скидка (%): ', min_value=1.0, max_value=100.0, step=0.5)

    count_button = st.button('Посчитать скидку')

    if count_button:
        flag = 1
        if not start_price:
            st.warning('ERROR: There is no start_price')
            flag = 0
        if not amount:
            st.warning('ERROR: There is no amount')
            flag = 0
        if not discount:
            st.warning('ERROR: There is no discount')
            flag = 0

        if flag:
            result = calculate_price(start_price, amount, discount)
            st.success(f'Цена со скидкой: {result}',icon="✅")
        else:
            st.warning('Check you Input Data')


    st.link_button("Go to Chat GPT", "https://chatgpt.com/")
