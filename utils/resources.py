import streamlit as st

def custom_sidebar():
    st.sidebar.subheader("Equipe - Grupo 45")
    st.sidebar.markdown("""
                        Alexandre Gomes de Araújo  
                        *RM 352922*

                        Fernando Tanese Mascara  
                        *RM 352656*

                        Jéssica Thesin Zulian  
                        *RM 353013*
                        """)

def config_pagina():
    st.set_page_config(
        page_title='Tech Challenge Fase 4',
        layout='wide'
    )
