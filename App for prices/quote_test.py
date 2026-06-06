import streamlit as st

title = st.title("Tolkien Quotes")
# question = st.header('**Where do you want your quote to be from?**')

select_movie = st.radio(
    '**Where do you want your quote to be from?**',
    ['Hobbit, pls :)', 'Lord of the Rings!', 'Have not decided yet'],
    index=2
)

if select_movie == 'Have not decided yet':
    st.write("**Choose a movie to see a quote ✨**")
elif select_movie == 'Hobbit, pls :)':
    st.write("***'The world is not in your books and maps. It is out there.'***")
    st.image('https://i0.wp.com/thesimplecatholic.blog/wp-content/uploads/2017/10/hobbit-going-on-an-adventure.gif?resize=616%2C247&ssl=1')
elif select_movie == 'Lord of the Rings!':
    st.write("***'Even the smallest person can change the course of the future.'***")
    st.image('https://64.media.tumblr.com/62c019f37383b06f6d3532b67ca9c25f/7ba043f07542ea9c-86/s540x810/87b370dbcf10ac02cd19e1870085b5f0b6de8764.gif')