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
dados.sort_values(by='DATA', ascending=True, inplace=True)
dados.reset_index(drop=True, inplace=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
                ##### Variação de preço no período

                No período que antecede a invasão do Kwait pelo Iraque, podemos ver uma ascenção \
                no preço, que se mantém em alta e bastante instável até próximo da liberação do país \
                pelas tropas lideradas pelos EUA. Após o término do conflito, o preço voltou a \
                patamares próximos do que era antes.
                """)
    dados_golfo = dados.loc[(dados['DATA'] >= '1990-01-01') & (dados['DATA'] <= '1991-07-31')].copy()
    dados_golfo.reset_index(drop=True, inplace=True)
    dados_golfo_hl = dados_golfo.loc[(dados_golfo['DATA'] >= '1990-08-02') & (dados_golfo['DATA'] <= '1991-02-28')].copy()
    dados_golfo_hl.reset_index(drop=True, inplace=True)
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
    with col2: st.plotly_chart(fig_golfo)


with st.expander('Crise asiática (1997)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Crise asiática - e outros fatores do final do século XX]", anchor=False)
    st.markdown("""
                A crise financeira asiática, que teve início em 1997, foi um período \
                de turbulência econômica que afetou várias economias do Sudeste Asiático, \
                levando a uma significativa queda na demanda por petróleo na região e contribuindo \
                para a queda dos preços em 1998. Esta crise começou na Tailândia, \
                com a desvalorização do baht, e rapidamente se espalhou para outros países \
                da região, resultando em uma série de desvalorizações monetárias, quedas \
                nas bolsas de valores e falências de empresas.

                A recuperação econômica começou a se manifestar em 1999, após uma combinação de \
                fatores internos e externos que ajudaram a estabilizar as economias afetadas e \
                promover o crescimento. Entre as ações que propiciaram a reversão do cenário de crise \
                podemos citar: a intervenção do FMI, com pacotes de resgate financeiro para os \
                países mais afetados, incluindo Tailândia, Indonésia e Coreia do Sul; reformas \
                econômicas nesses países, incluindo a reestruturação do setor financeiro, a \
                melhoria da governança corporativa e a liberalização de mercados, que ajudaram a resolver \
                problemas de insolvência e a restaurar a confiança internacional; e a desvalorização \
                das moedas durante a crise, que embora tenha sido parte do problema, no médio prazo\
                tornou as exportações asiáticas mais competitivas no mercado global e acabou por atrair \
                investidores estrangeiros.
                
                Paralelamente ao cenário de dificuldade econômica da Ásia, a OPEP e alguns países não membros, \
                como o México, acordaram em reduzir a produção de petróleo em 1998, para estabilizar \
                os preços que estavam em queda. Este esforço conjunto foi reforçado em março de 1999, \
                quando a OPEP implementou novos cortes de produção, ajudando a reduzir o excesso de \
                oferta e a estabilizar o mercado.

                Adicionalmente, a recuperação das economias asiáticas e o crescimento econômico global, \
                especialmente nos Estados Unidos, aumentaram a demanda por petróleo. Embora o final \
                dos anos 1990 não tenha testemunhado grandes conflitos que impactassem diretamente a produção \
                de petróleo, a instabilidade política em algumas regiões produtoras e a especulação nos mercados \
                financeiros adicionaram uma camada de incerteza que influenciou os preços. Esses fatores \
                combinados contribuíram para a ascensão dos preços do petróleo a partir de fevereiro de 1999, \
                marcando o fim de um período de baixa e o início de uma nova fase de recuperação do mercado.

                """
                )
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
                ##### Variação de preço no período

                A data de 02/07/97 marca o início da crise, e após uma pequena guinada para cima, o preço\
                entra em uma evidente queda. No meio dessa descida, ocorrem os dois acordos da OPEP \
                (jul/1998 e mar/1999) para cortar a produção e tentar conter a derrocada. A data de 31/03/1999 \
                marca o fim do período de interesse, após o qual vemos uma forte ascensão do preço do \
                petróleo, acima da média do período anterior à crise.
                """)
    dados_asia = dados.loc[(dados['DATA'] >= '1996-01-01') & (dados['DATA'] <= '2000-12-31')].copy()
    dados_asia.reset_index(drop=True, inplace=True)
    dados_asia_hl = dados_asia.loc[(dados_asia['DATA'] >= '1997-07-02') & (dados_asia['DATA'] <= '1999-03-31')].copy()
    dados_asia_hl.reset_index(drop=True, inplace=True)
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
    with col2: st.plotly_chart(fig_asia)


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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                Bla.
                """)
    dados_terror = dados.loc[(dados['DATA'] >= '2000-07-01') & (dados['DATA'] <= '2005-07-31')].copy()
    dados_terror.reset_index(drop=True, inplace=True)
    dados_terror_hl = dados_terror.loc[(dados_terror['DATA'] >= '2001-09-11') & (dados_terror['DATA'] <= '2003-12-31')].copy()
    dados_terror_hl.reset_index(drop=True, inplace=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                Bla.
                """)
    dados_crise = dados.loc[(dados['DATA'] >= '2007-01-01') & (dados['DATA'] <= '2009-12-31')].copy()
    dados_crise.reset_index(drop=True, inplace=True)
    dados_crise_hl = dados_crise.loc[(dados_crise['DATA'] >= '2008-03-14') & (dados_crise['DATA'] <= '2009-02-17')].copy()
    dados_crise_hl.reset_index(drop=True, inplace=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                Bla.
                """)
    dados_prim = dados.loc[(dados['DATA'] >= '2009-07-01') & (dados['DATA'] <= '2014-12-31')].copy()
    dados_prim.reset_index(drop=True, inplace=True)
    dados_prim_hl = dados_prim.loc[(dados_prim['DATA'] >= '2010-12-17') & (dados_prim['DATA'] <= '2013-12-31')].copy()
    dados_prim_hl.reset_index(drop=True, inplace=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                Bla.
                """)
    dados_ofdem = dados.loc[(dados['DATA'] >= '2013-01-01') & (dados['DATA'] <= '2017-12-31')].copy()
    dados_ofdem.reset_index(drop=True, inplace=True)
    dados_ofdem_hl = dados_ofdem.loc[(dados_ofdem['DATA'] >= '2014-11-26') & (dados_ofdem['DATA'] <= '2016-11-30')].copy()
    dados_ofdem_hl.reset_index(drop=True, inplace=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                Bla.
                """)
    dados_pandemia = dados.loc[(dados['DATA'] >= '2019-01-01') & (dados['DATA'] <= '2023-12-31')].copy()
    dados_pandemia.reset_index(drop=True, inplace=True)
    dados_pandemia_hl = dados_pandemia.loc[(dados_pandemia['DATA'] >= '2020-03-11') & (dados_pandemia['DATA'] <= '2022-12-31')].copy()
    dados_pandemia_hl.reset_index(drop=True, inplace=True)
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
