import streamlit as st

def custom_sidebar():
    st.sidebar.subheader("Equipe")
    st.sidebar.markdown("Alexandre Gomes de Araujo")
    st.sidebar.markdown("*RM 123456789*")
    st.sidebar.markdown("Fernando Tanese Mascara")
    st.sidebar.markdown("*RM 123456789*")
    st.sidebar.markdown("Jessica Thesin Zulian")
    st.sidebar.markdown("*RM 123456789*")

def config_pagina():
    st.set_page_config(
        page_title='Tech Challenge Fase 4',
        layout='wide'
    )