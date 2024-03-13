import streamlit as st


class st_style:
    def config_page(page_title, page_icon):
        st.set_page_config(
            page_title = page_title,
            page_icon = page_icon
        )


    def hide_header():
        hide_decoration_bar_style = '''
        <style>
            header {visibility: hidden;}
        </style>
        '''
        st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)