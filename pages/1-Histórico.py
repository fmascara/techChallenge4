import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils.resources import custom_sidebar, config_pagina

config_pagina()

custom_sidebar()

## FUNÇÕES:
def formata_numero(valor):
    return f'{valor:.2f}'

## TABELAS:
dados = pd.read_csv('tabela preliminar ipea.txt', sep='\t')
dados['PREÇO'] = dados['PREÇO'].str.replace(',', '.')
dados['PREÇO'] = dados['PREÇO'].astype(float)
dados['DATA'] = pd.to_datetime(dados['DATA'], format='%d/%m/%Y')
dados['MÊS'] = dados['DATA'].dt.month_name()
dados['ANO'] = dados['DATA'].dt.year.astype(str)

stats = dados.describe()

eventos = {
    'EVENTO': [
        'Guerra do Golfo',
        'Atentados terroristas nos EUA',
        'Guerra do Iraque',
        'Crise financeira global',
        'Primavera Árabe',
        'Grande produção e baixa demanda',
        'Pandemia de COVID-19',
        'Conflito Rússia-Ucrânia'
    ],
    'DATA INÍCIO': [
        '1990-08-02',
        '2001-09-11',
        '2003-03-20',
        '2008-03-14',
        '2010-12-17',
        '2014-11-26',
        '2020-03-11',
        '2022-02-24'
    ],
    'DATA FIM': [
        '1991-02-28',
        '2001-09-11',
        '2011-12-15',
        '2009-02-17',
        '2013-12-31',
        '2016-11-30',
        '2022-12-31',
        '2023-02-24'
    ]
}
df_eventos = pd.DataFrame(eventos)
df_eventos['DATA INÍCIO'] = pd.to_datetime(df_eventos['DATA INÍCIO'])
df_eventos['DATA FIM'] = pd.to_datetime(df_eventos['DATA FIM'])

## VISUALIZAÇÃO:
st.subheader(
    ":red[Tech Challenge Fase 4]",
    divider="red",
)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Histórico do petróleo Brent')
st.write('O Petróleo Brent, também conhecido como Brent Blend, \
            é um tipo de petróleo bruto leve e doce extraído do Mar \
            do Norte, entre a Noruega e o Reino Unido. Apesar de \
            não ser o tipo mais produzido atualmente no mundo, \
            ele desempenha um papel crucial no mercado global de petróleo.')
st.write('O preço do Brent é o principal referencial para a \
            indústria petrolífera, servindo de padrão global para \
            a precificação de outros tipos de petróleo, e de base para a negociação \
            de contratos futuros e derivativos. Quando se diz que o \
            petróleo "subiu" ou "desceu", é do preço do Brent que \
            se está falando. Devido a essa importância, sua cotação \
            serve de medida para decisões da OPEP (Organização dos \
            Países Exportadores de Petróleo).')
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,1])
with col1:
    st.subheader('Variação do preço do Brent ao longo do tempo')
with col2:
    ano_inicial = st.slider('Ano inicial na visualização', min_value=dados['DATA'].dt.year.min(), 
                    max_value=dados['DATA'].dt.year.max(), 
                    value=dados['DATA'].dt.year.min(), step=1)
with col3:
    ano_final = st.slider('Ano final na visualização', min_value=dados['DATA'].dt.year.min(), 
                    max_value=dados['DATA'].dt.year.max(), 
                    value=dados['DATA'].dt.year.max(), step=1)
dados_filtrados = dados[(dados['DATA'].dt.year >= ano_inicial) & (dados['DATA'].dt.year <= ano_final)]
df_eventos_filtrados = df_eventos[(df_eventos['DATA INÍCIO'].dt.year >= ano_inicial) & (df_eventos['DATA INÍCIO'].dt.year <= ano_final)]
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dados_filtrados['DATA'],
    y=dados_filtrados['PREÇO'],
    mode='lines',
    name='Preço Diário'
))  
for i, row in df_eventos_filtrados.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['DATA INÍCIO']],
        y=[dados_filtrados.set_index('DATA').loc[row['DATA INÍCIO']]['PREÇO']],
        mode='markers+text',
        marker=dict(size=12, color='red'),
        text=str(i+1),
        textposition="top left",
        textfont=dict(size=16),
        name=f"{i+1} - {row['EVENTO']}"
    ))
fig.update_layout(
    legend=dict(
        orientation="h",  # Horizontal
        yanchor="bottom",  # Ancorar ao fundo
        y=-0.8,  # Colocar a legenda abaixo do gráfico
        xanchor="center",  # Centralizar horizontalmente
        x=0.5  # Posicionar no centro
    ),
    xaxis_title="Data",  # Label do eixo x
    yaxis_title="Preço (US$)",  # Label do eixo y
)
st.plotly_chart(fig)
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader('Eventos históricos relevantes para a variação do preço')
with st.expander('Guerra do Golfo (1990)', expanded=False):
    st.write('')
with st.expander('Atentado terrorista de 11/09/2001', expanded=False):
    st.write('')
with st.expander('Guerra do Iraque (2003)', expanded=False):
    st.write('')
with st.expander('Crise financeira global (2008)', expanded=False):
    st.write('')
with st.expander('Primavera Árabe (2010)', expanded=False):
    st.write('')
with st.expander('Alta oferta, baixa demanda (2014)', expanded=False):
    st.write('')
with st.expander('Pandemia de COVID-19 (2020)', expanded=False):
    st.write('')
with st.expander('Conflito Rússia-Ucrânia (2022)', expanded=False):
    st.write('')