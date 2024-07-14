import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from scipy.stats import gaussian_kde
from utils.resources import custom_sidebar, config_pagina

config_pagina()

custom_sidebar()

## FUNÇÕES:
def formata_numero(valor):
    return f'{valor:.2f}'

## TABELAS:
dados = pd.read_csv('https://raw.githubusercontent.com/fmascara/techChallenge4/main/tabela_preliminar_ipea.txt', sep='\t')
dados['PREÇO'] = dados['PREÇO'].str.replace(',', '.')
dados['PREÇO'] = dados['PREÇO'].astype(float)
dados['DATA'] = pd.to_datetime(dados['DATA'], format='%d/%m/%Y')
dados.sort_values(by='DATA', ascending=True, inplace=True)
dados.reset_index(drop=True, inplace=True)

dados_seg = dados.loc[dados['DATA'] >= '2020-01-01'].copy()
dados_seg.reset_index(drop=True, inplace=True)

stats = dados.describe()
stats_seg = dados_seg.describe()

## VISUALIZAÇÃO
st.subheader(":red[Tech Challenge Fase 4]", divider="red", anchor=False)
st.markdown("<br>", unsafe_allow_html=True)
st.subheader('Análise Exploratória', anchor=False)
st.markdown("""
            Dentro da nossa base de dados, estamos analisando informações desde \
            20/05/1987 a 18/06/2024, e apresentamos a seguir a análise descritiva \
            da distribuição dos preços de petróleo ao longo do período estudado.  
            
            Observa-se que temos 11.194 registros, com uma média de 53,08 e desvio \
            padrão de 33,22. O valor mínimo observado é de 9,10 e o máximo é de 143,95. \
            Fazendo uma análise mais particionada, podemos avaliar os quartis, sendo \
            que 25% estão abaixo de 20,50, 50% estão abaixo de 48,35 e 75% estão abaixo \
            de 76,42.
            """)

col1, col2, col3 = st.columns([5,1,6])
with col1: 
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Estatística descritiva")
    st.dataframe(stats)
with col3:
    fig1 = px.box(dados, y='PREÇO', title='Distribuição dos Preços')
    st.plotly_chart(fig1)

st.markdown("""
            Já para as previsões, segmentamos os nossos dados, considerando apenas as \
            ocorrências mais recentes. Sendo assim, estamos usando informações desde 01/01/2020 \
            a 18/06/2024, e apresentamos a seguir a análise descritiva da distribuição dos \
            preços de petróleo ao longo do período segmentado.

            Observa-se que temos 1.135 registros, com uma média de 74,89 e desvio padrão \
            de 22,88. O valor mínimo observado é de 9,12 e o máximo é de 133,18. Fazendo uma \
            análise mais particionada, podemos avaliar os quartis, sendo que 25% estão abaixo \
            de 63,23, 50% estão abaixo de 78,72 e 75% estão abaixo de 87,37.
            """)
col1, col2, col3 = st.columns([5,1,6])
with col1: 
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Estatística descritiva (segmentação)")
    st.dataframe(stats_seg)
with col3:
    fig2 = px.box(dados_seg, y='PREÇO', title='Distribuição dos Preços (segmentação)')
    st.plotly_chart(fig2)

st.markdown("##### Por que segmentar?")
st.markdown("""
            A comparação dos boxplots de cada conjunto de dados deixa clara as diferenças entre eles. \
            No dataset completo, com todos os registros desde mai/1987, os preços que \
            mais aparecem estão entre 76,57 e 20,25, enquanto que no conjunto segmentado, \
            com registros a partir de jan/2020, os preços estão concentrados em um espaço \
            muito menor e "mais alto", entre 87,38 e 63,20. Além disso, no segundo caso, \
            valores abaixo de 26 e acima de 123 são representados como \
            outliers, coisa que não acontece no primeiro.

            Podemos enxergar com mais clareza a diferença, comparando lado a lado a distribuição dos \
            valores dos dois datasets em histogramas. Observamos que a concentração de valores \
            em torno de 14 a 26 no primeiro não se repete no segundo, no qual a concentração maior fica \
            em torno de 70 a 90. Ao longo do tempo, o patamar dos preços do petróleo subiu \
            consideravelmente, então, para a aplicação de modelos de previsão, faz todo o sentido \
            segmentar no tempo e aproveitar apenas os valores mais recentes.
            """)
fig_hist = px.histogram(dados, x='PREÇO', nbins=100, title='Histograma dos Preços (1987 a 2024)')
fig_hist_seg = px.histogram(dados_seg, x='PREÇO', nbins=100, title='Histograma dos Preços (2020 a 2024)')
col1, col2 = st.columns(2)
with col1: st.plotly_chart(fig_hist)
with col2: st.plotly_chart(fig_hist_seg)
