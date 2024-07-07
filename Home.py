import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils.resources import custom_sidebar, config_pagina

config_pagina()

## FUNÇÕES:
def formata_numero(valor):
    return f'{valor:.2f}'

## VISUALIZAÇÃO:
custom_sidebar()

st.subheader(
    ":red[Tech Challenge Fase 4]",
    divider="red",
)

st.title('Estudos sobre o preço do petróleo tipo Brent')
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Sobre este trabalho')
st.write('O presente estudo foi elaborado como resposta ao Tech Challenge da Fase 4.')
st.write('Os objetivos aqui são dois:')
lista_objetivos = """
1. Analisar os dados históricos de preço do petróleo Brent \
    e desenvolver um dashboard interativo que possa levar \
    a insights relevantes para tomadas de decisões.
2. Fazer a previsão dos preços futuros desenvolvendo e \
    aplicando um modelo de machine learning.
"""
st.write(lista_objetivos)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Fontes dos dados')
st.write('Os preços para este estudo foram obtidos no site\
            do IPEA, mas são provenientes originalmente da EIA.')
st.write('IPEA - Instituto de Pesquisa Econômica Aplicada - \
            é uma fundação pública federal vinculada ao Ministério \
            da Economia. Suas atividades de pesquisa fornecem suporte \
            técnico e institucional às ações governamentais para a \
            formulação e reformulação de políticas públicas e programas \
            de desenvolvimento brasileiros. O Ipea é responsável pelo \
            levantamento e divulgação de dados econômicos do Brasil, \
            e seu trabalho serve de base para ações governamentais em diversas áreas.')
st.write('EIA - Energy Information Administration - é uma agência \
            governamental dos Estados Unidos formada em 1977. Sua missão \
            é coletar, analisar e disseminar informações independentes \
            e imparciais sobre energia, promovendo a formulação de \
            políticas sólidas, mercados eficientes e compreensão pública \
            sobre a energia e sua interação com a economia e o meio ambiente. ')
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Referências')


