import streamlit as st

def custom_sidebar():
    st.sidebar.subheader("Equipe")
    st.sidebar.markdown("Alexandre Gomes de Araujo")
    st.sidebar.markdown("*RM 352922*")
    st.sidebar.markdown("Fernando Tanese Mascara")
    st.sidebar.markdown("*RM 352656*")
    st.sidebar.markdown("Jessica Thesin Zulian")
    st.sidebar.markdown("*RM 353013*")

def config_pagina():
    st.set_page_config(
        page_title='Tech Challenge Fase 4',
        layout='wide'
    )
