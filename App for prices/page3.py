import streamlit as st

def page_3():
    st.title('Page 3')


col1, col2 = st.columns(2)

with col1:
    st.header('A dog')
    st.image('https://plus.unsplash.com/premium_photo-1694819488591-a43907d1c5cc?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZG9nJTIwYnJlZWRzfGVufDB8fDB8fHww')
with col2:
    st.header('An owl')
    st.image('https://libertywildlife.org/wp-content/uploads/2024/10/liberty-wildlife-profile-willis.jpg')

row1 = st.columns(2)
row2 = st.columns(2)

for col in row1 + row2:
    tile = col.container(height=200, horizontal=True, horizontal_alignment='center', vertical_alignment='center')
    tile.write("Very nice day to start programming")

words = ["Very", "nice", "day", "to", "start", "programming"]

row1 = st.columns(3)
row2 = st.columns(3)

all_cols = row1 + row2

for col, word in zip(all_cols, words):
    tile = col.container(height=120, horizontal=True, horizontal_alignment='center', vertical_alignment='center')
    tile.write(word)