import streamlit as st

def main():

    pages = {
        "Pages": [
            st.Page("page1.py", title="Go to Page 1"),
            st.Page("page2.py", title="Go to Page 2"),
            st.Page("page3.py", title='Go to Page 3')
        ]
        , 'Tolkien Quotes Page': [
            st.Page("quote_test.py", title='Tolkien Quotes')]
    }

    pg = st.navigation(pages, position="top")
    pg.run()




if __name__ == '__main__':
    main()

