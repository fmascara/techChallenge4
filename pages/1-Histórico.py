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
        'Crise Asiática',
        'Guerra ao Terror',
        'Crise financeira global',
        'Primavera Árabe',
        'Grande produção e baixa demanda',
        'Pandemia de COVID-19'
    ],
    'DATA INÍCIO': [
        '1990-08-02',
        '1997-07-02',
        '2001-09-11',
        '2008-03-14',
        '2010-12-17',
        '2014-11-26',
        '2020-03-11'
    ],
    'DATA FIM': [
        '1991-02-28',
        '1999-03-31',
        '2011-12-15',
        '2009-02-17',
        '2013-12-31',
        '2016-11-30',
        '2022-12-31'
    ]
}
df_eventos = pd.DataFrame(eventos)
df_eventos['DATA INÍCIO'] = pd.to_datetime(df_eventos['DATA INÍCIO'])
df_eventos['DATA FIM'] = pd.to_datetime(df_eventos['DATA FIM'])





## INÍCIO DA VISUALIZAÇÃO:
st.subheader(":red[Tech Challenge Fase 4]", divider="red", anchor=False)
st.markdown("<br>", unsafe_allow_html=True)
st.subheader('Histórico do petróleo Brent', anchor=False)
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
    st.subheader('Variação do preço do Brent ao longo do tempo', anchor=False)
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
    name='Preço'
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
    xaxis_title="Data",
    yaxis_title="Preço (US$)"
)
st.plotly_chart(fig)
st.markdown("<br><br>", unsafe_allow_html=True)





st.subheader('Relação entre os eventos históricos e o preço', anchor=False)

with st.expander(('Guerra do Golfo (1990)'), expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Guerra do Golfo]", anchor=False)
    st.write('A Guerra do Golfo aconteceu entre 02 de agosto de 1990 e 28 de fevereiro de 1991 no \
             Oriente Médio. O conflito teve como motivação a invasão do Kuwait por tropas do Iraque, \
             sob o regime de Saddam Hussein, resultando em uma coalizão internacional com o intuito \
             de expulsar as tropas iraquianas.')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Reminiscências da Guerra Irã-Iraque:** Após a longa e custosa Guerra Irã-Iraque \
                (1980-1988), o Iraque estava profundamente endividado, principalmente com o \
                Kuwait e a Arábia Saudita. O Iraque acusava o Kuwait de roubar petróleo da reserva \
                de Rumaila, que se estendia pela fronteira entre os dois países. Além disso, o \
                Iraque alegava que o Kuwait estava excedendo suas quotas de produção de petróleo \
                estabelecidas pela OPEP, contribuindo para a queda dos preços do petróleo, o que \
                prejudicava a economia iraquiana.
                * **Riqueza Petrolífera do Kuwait:** A invasão do Kuwait pelo Iraque foi, em parte, \
                motivada pelo desejo de Saddam Hussein de controlar as vastas reservas de petróleo \
                do Kuwait, que eram uma das maiores do mundo. O controle sobre essas reservas \
                fortaleceria significativamente a posição econômica e política do Iraque.

                ##### Consequências Relacionadas ao Petróleo:
                * **Aumento e Oscilação dos Preços:** Durante o conflito, houve volatilidade nos preços,\
                 que aumentaram com o início da guerra e voltaram a cair após a rápida vitória da coalizão \
                e a segurança relativa do fornecimento de petróleo.
                * **Sanções Econômicas:** Após a guerra, o Iraque enfrentou severas sanções econômicas \
                impostas pelas Nações Unidas, que incluíam restrições à exportação de petróleo. Estas \
                sanções tiveram um impacto devastador na economia iraquiana.
                * **Mudanças na OPEP:** A guerra destacou a importância da estabilidade no mercado \
                de petróleo e levou a uma maior cooperação entre os membros da OPEP para regular a \
                produção e estabilizar os preços do petróleo.
                """
                )
    dados_golfo = dados.loc[(dados['DATA'] >= '1990-01-01') & (dados['DATA'] <= '1991-07-31')].copy().reset_index()
    dados_golfo_hl = dados_golfo.loc[(dados_golfo['DATA'] >= '1990-08-02') & (dados_golfo['DATA'] <= '1991-02-28')]
    fig_golfo = go.Figure()
    fig_golfo.add_trace(go.Scatter(
        x=dados_golfo['DATA'],
        y=dados_golfo['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_golfo.add_trace(go.Scatter(
        x=dados_golfo_hl['DATA'],
        y=dados_golfo_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_golfo.update_layout(
        yaxis=dict(range=[0, 60]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_golfo)


with st.expander('Crise asiática (1997)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Crise asiática]", anchor=False)
    st.write('Bla')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_asia = dados.loc[(dados['DATA'] >= '1996-01-01') & (dados['DATA'] <= '2000-12-31')].copy().reset_index()
    dados_asia_hl = dados_asia.loc[(dados_asia['DATA'] >= '1997-07-02') & (dados_asia['DATA'] <= '1999-03-31')]
    fig_asia = go.Figure()
    fig_asia.add_trace(go.Scatter(
        x=dados_asia['DATA'],
        y=dados_asia['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_asia.add_trace(go.Scatter(
        x=dados_asia_hl['DATA'],
        y=dados_asia_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_asia.update_layout(
        yaxis=dict(range=[0, 50]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_asia)


with st.expander('Guerra ao Terror (2001)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Guerra ao Terror]", anchor=False)
    st.write('Após sofrer com os atentados de 11 de setembro de 2001, os Estados Unidos \
             decidiram empreender uma “guerra contra o terror” apontando os governos que \
             poderiam representar riscos à paz mundial. Nesse sentido, o presidente norte-americano \
             George W. Bush e seu Conselho de Estado passaram a fazer uma campanha política \
             pregando a intervenção no chamado “eixo do mal”. Entre os países que compunham esse \
             grupo, estariam o Afeganistão, berço da Al-Qaeda - grupo responsável por \
             coordenar os ataques - e o Iraque, ainda liderado pelo ditador Saddam Hussein.\
             A Guerra ao Terror teve um impacto combinado significativo no mercado de petróleo, \
             influenciando tanto a oferta quanto a demanda, além de adicionar \
             uma camada de risco geopolítico que afetou os preços do petróleo a longo prazo.')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_terror = dados.loc[(dados['DATA'] >= '2000-07-01') & (dados['DATA'] <= '2005-07-31')].copy().reset_index()
    dados_terror_hl = dados_terror.loc[(dados_terror['DATA'] >= '2001-09-11') & (dados_terror['DATA'] <= '2003-12-31')]
    fig_terror = go.Figure()
    fig_terror.add_trace(go.Scatter(
        x=dados_terror['DATA'],
        y=dados_terror['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_terror.add_trace(go.Scatter(
        x=dados_terror_hl['DATA'],
        y=dados_terror_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_terror.update_layout(
        yaxis=dict(range=[0, 60]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_terror)


with st.expander('Crise financeira global (2008)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Crise financeira global]", anchor=False)
    st.write('Bla')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_crise = dados.loc[(dados['DATA'] >= '2007-01-01') & (dados['DATA'] <= '2009-12-31')].copy().reset_index()
    dados_crise_hl = dados_crise.loc[(dados_crise['DATA'] >= '2008-03-14') & (dados_crise['DATA'] <= '2009-02-17')]
    fig_crise = go.Figure()
    fig_crise.add_trace(go.Scatter(
        x=dados_crise['DATA'],
        y=dados_crise['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_crise.add_trace(go.Scatter(
        x=dados_crise_hl['DATA'],
        y=dados_crise_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_crise.update_layout(
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_crise)


with st.expander('Primavera Árabe (2010)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Primavera Árabe]", anchor=False)
    st.write('Bla')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_prim = dados.loc[(dados['DATA'] >= '2009-07-01') & (dados['DATA'] <= '2014-12-31')].copy().reset_index()
    dados_prim_hl = dados_prim.loc[(dados_prim['DATA'] >= '2010-12-17') & (dados_prim['DATA'] <= '2013-12-31')]
    fig_prim = go.Figure()
    fig_prim.add_trace(go.Scatter(
        x=dados_prim['DATA'],
        y=dados_prim['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_prim.add_trace(go.Scatter(
        x=dados_prim_hl['DATA'],
        y=dados_prim_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_prim.update_layout(
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_prim)


with st.expander('Alta oferta, baixa demanda (2014)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Período de alta oferta e baixa demanda]", anchor=False)
    st.write('Bla')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_ofdem = dados.loc[(dados['DATA'] >= '2013-01-01') & (dados['DATA'] <= '2017-12-31')].copy().reset_index()
    dados_ofdem_hl = dados_ofdem.loc[(dados_ofdem['DATA'] >= '2014-11-26') & (dados_ofdem['DATA'] <= '2016-11-30')]
    fig_ofdem = go.Figure()
    fig_ofdem.add_trace(go.Scatter(
        x=dados_ofdem['DATA'],
        y=dados_ofdem['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_ofdem.add_trace(go.Scatter(
        x=dados_ofdem_hl['DATA'],
        y=dados_ofdem_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_ofdem.update_layout(
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_ofdem)


with st.expander('Pandemia de COVID-19 (2020)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Pandemia de COVID-19]", anchor=False)
    st.write('Bla')
    st.markdown("""
                ##### Causas Relacionadas ao Petróleo:
                * **Bla:** Bla.

                ##### Consequências Relacionadas ao Petróleo:
                * **Bla:** Bla
                """
                )
    dados_pandemia = dados.loc[(dados['DATA'] >= '2019-01-01') & (dados['DATA'] <= '2023-12-31')].copy().reset_index()
    dados_pandemia_hl = dados_pandemia.loc[(dados_pandemia['DATA'] >= '2020-03-11') & (dados_pandemia['DATA'] <= '2022-12-31')]
    fig_pandemia = go.Figure()
    fig_pandemia.add_trace(go.Scatter(
        x=dados_pandemia['DATA'],
        y=dados_pandemia['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_pandemia.add_trace(go.Scatter(
        x=dados_pandemia_hl['DATA'],
        y=dados_pandemia_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_pandemia.update_layout(
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    st.plotly_chart(fig_pandemia)
