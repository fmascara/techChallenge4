import streamlit as st
import pandas as pd
import numpy as np
import joblib  # ou pickle, dependendo de como você salvou seu modelo
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from utils.resources import custom_sidebar, config_pagina

config_pagina()

custom_sidebar()

## FUNÇÕES:
def formata_numero(valor):
    return f'{valor:.2f}'

# Carregar os dados
#previsao_prophet = pd.read_csv('previsao_prophet.csv', sep=',') #depois mudar pro caminho do git
previsao_prophet = pd.read_csv('https://raw.githubusercontent.com/fmascara/techChallenge4/main/previsao_prophet.csv')
previsao_prophet['ds'] = pd.to_datetime(previsao_prophet['ds'])  # Converter a coluna 'ds' para datetime
previsao_prophet['trend'] = round(previsao_prophet['trend'],2)
previsao_prophet = previsao_prophet.rename(columns={'ds':'DATA','trend':'PREVISÃO'})
previsao_prophet = previsao_prophet.query("DATA > '2024-06-20'")

#previsao_lstm = pd.read_csv('previsao_lstm.csv', sep=',') #depois mudar pro caminho do git
previsao_lstm = pd.read_csv('https://raw.githubusercontent.com/fmascara/techChallenge4/main/previsao_lstm.csv')
previsao_lstm['ds'] = pd.to_datetime(previsao_lstm['ds'])  # Converter a coluna 'ds' para datetime
previsao_lstm['previsao'] = round(previsao_lstm['previsao'],2)
previsao_lstm = previsao_lstm.rename(columns={'ds':'DATA','previsao':'PREVISÃO'})
previsao_lstm = previsao_lstm.query("DATA > '2024-06-20'")

dados_reais = pd.read_csv('https://raw.githubusercontent.com/fmascara/techChallenge4/main/tabela_precos_2024.txt', sep='\t')
dados_reais['PREÇO'] = dados_reais['PREÇO'].str.replace(',', '.')
dados_reais['PREÇO'] = dados_reais['PREÇO'].astype(float)
dados_reais['DATA'] = pd.to_datetime(dados_reais['DATA'], format='%d/%m/%Y')
dados_reais = dados_reais.loc[(dados_reais['DATA'] >= '2024-04-01')]
dados_reais.sort_values(by='DATA', ascending=True, inplace=True)

########################### STREAMLIT ##########################
st.subheader(":red[Tech Challenge Fase 4]", divider="red", anchor=False)
st.markdown("<br>", unsafe_allow_html=True)
st.subheader('Previsão do preço do barril de petróleo Brent', anchor=False)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
            Nesta análise, para prever o preço do barril de petróleo em diferentes períodos, \
            optamos em utilizar os modelos PROPHET e LSTM, uma vez que, o primeiro modelo, \
            apresenta bons comportamentos ao analisar padrões sazonais robustos e complexos, \
            enquanto o segundo, ao lidar com redes neurais, tem bom desempenho ao avaliar longos \
            períodos. Ambos, apresentam boas atuações ao avaliar a série temporal considerando \
            comportamentos exógenos ao modelo, mas que de certa forma, tem correlação direta.
            """)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Definindo as abas
tabs = st.tabs(["Previsão com o Prophet", "Previsão com o LSTM", "Métricas de performance", "Insight das medidas de erros dos modelos"])

# Conteúdo da Aba 1
with tabs[0]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Previsão com o modelo Prophet]", anchor=False)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
            O modelo Prophet foi desenvolvido pela Meta e é uma ótima ferramenta para previsão \
            de séries temporais, para casos cujas características apresentem sazonalidade, \
            tendências não lineares e feriados.
            """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True, height=150):
        st.markdown("#### Resultados de performance obtidos")
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("### MSE: 11,36%")
        with col2: st.markdown("### RMSE: 3,37%")
        with col3: st.markdown("### MAPE: 4,04%")
    
    st.markdown("<br>", unsafe_allow_html=True)

    
    # Data inicial fixa
    start_date = datetime(2024, 6, 21)

    # Data final padrão
    end_date_default = datetime(2024, 7, 20)
    max_date = end_date_default

    # Criar o campo de seleção de data para a data final
    col1, col2, col3, col4 = st.columns([3.5,2,1,3.5])
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Selecione a data final da previsão:")
    with col2:
        end_date = st.slider(
            '',
            min_value=start_date,
            max_value=end_date_default,
            value=start_date,
            format="YYYY-MM-DD",
            key='slider1'
        )
    with col4:
        # Mostrar as datas selecionadas
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(f'Data inicial fixa de previsão: {start_date.date()}')
        st.write(f'Data final da previsão: {end_date.date()}')


    def consultar_eventos(end_date):
        if end_date == max_date:
            # Se a data final for a máxima, mostrar toda a tabela
            resultados = previsao_prophet
        else:
            # Caso contrário, mostrar a consulta com as datas especificadas
            resultados = previsao_prophet[(previsao_prophet['DATA'] >= start_date) & (previsao_prophet['DATA'] <= end_date)]
        return resultados

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button('Buscar Previsão', key='button1'):
        # Realizar a consulta e obter os resultados
        resultados = consultar_eventos(end_date)

        # Mostrar os resultados
        if not resultados.empty:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.write("Eventos até a data final informada:")
            # Converter o DataFrame para HTML sem o índice
            col1, col2 = st.columns([2,5])
            with col1: st.write(resultados.to_html(index=False), unsafe_allow_html=True)
            with col2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=dados_reais['DATA'],
                    y=dados_reais['PREÇO'],
                    mode='lines',
                    line=dict(width=3),
                    name='Preços reais'
                )) 
                fig.add_trace(go.Scatter(
                    x=resultados['DATA'],
                    y=resultados['PREVISÃO'],
                    mode='lines',
                    line=dict(width=3),
                    name='Previsão'
                ))
                fig.update_layout(
                    yaxis=dict(range=[60, 100]),
                    xaxis_title='Data',
                    yaxis_title='Preço (US$)'
                )
                st.plotly_chart(fig)
        else:
            st.write("Não há eventos até a data final informada.")

# Conteúdo da Aba 2 - LSTM
with tabs[1]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Previsão com o modelo LSTM]", anchor=False)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
            O LSTM é um modelo de rede neural recorrente, que lida com sequências de dados e \
            consegue capturar dependências de longo prazo.
            """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True, height=150):
        st.markdown("#### Resultados de performance obtidos")
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("### MSE: 0,0000102502%")
        with col2: st.markdown("### RMSE: 0,3202%")
        with col3: st.markdown("### MAPE: 2,80%")

    st.markdown("<br>", unsafe_allow_html=True)
        
    # Data inicial fixa
    start_date2 = datetime(2024, 6, 21)

    # Data final padrão
    end_date_default2 = datetime(2024, 7, 20)
    max_date2 = end_date_default2

    # Criar o campo de seleção de data para a data final
    col1, col2, col3, col4 = st.columns([3.5,2,1,3.5])
    with col1: 
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Selecione a data final da previsão:")
    with col2:
        end_date2 = st.slider(
            '',
            min_value=start_date2,
            max_value=end_date_default2,
            value=start_date2,
            format="YYYY-MM-DD",
            key='slider2'
        )
    with col4:
        # Mostrar as datas selecionadas
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(f'Data inicial fixa de previsão: {start_date2.date()}')
        st.write(f'Data final da previsão: {end_date2.date()}')


    def consultar_eventos2(end_date2):
        if end_date2 == max_date2:
            # Se a data final for a máxima, mostrar toda a tabela
            resultados2 = previsao_lstm
        else:
            # Caso contrário, mostrar a consulta com as datas especificadas
            resultados2 = previsao_lstm[(previsao_lstm['DATA'] >= start_date2) & (previsao_lstm['DATA'] <= end_date2)]
        return resultados2

    st.markdown("<br>", unsafe_allow_html=True)


    if st.button('Buscar Previsão', key='button2'):
        # Realizar a consulta e obter os resultados
        resultados2 = consultar_eventos2(end_date2)

        # Mostrar os resultados
        if not resultados2.empty:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.write("Eventos até a data final informada:")
            # Converter o DataFrame para HTML sem o índice
            col1, col2 = st.columns([2,5])
            with col1: st.write(resultados2.to_html(index=False), unsafe_allow_html=True)
            with col2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=dados_reais['DATA'],
                    y=dados_reais['PREÇO'],
                    mode='lines',
                    line=dict(width=3),
                    name='Preços reais'
                )) 
                fig.add_trace(go.Scatter(
                    x=resultados2['DATA'],
                    y=resultados2['PREVISÃO'],
                    mode='lines',
                    line=dict(width=3),
                    name='Previsão'
                ))
                fig.update_layout(
                    yaxis=dict(range=[60, 100]),
                    xaxis_title='Data',
                    yaxis_title='Preço (US$)'
                )
                st.plotly_chart(fig)
        else:
            st.write("Não há eventos até a data final informada.")
        
with tabs[2]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Medição da performance]", anchor=False)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                A performance dos modelos preditivos é analisada a partir das seguintes métricas:

                * **MSE (Mean Squared Error):** o erro quadrático médio, é utilizado para verificar \
                a acurácia dos modelos e dá maior peso aos maiores erros. É uma métrica bastante \
                sensível a outliers e coloca bastante peso nas previsões com erros mais expressivos. \
                Quanto menor o valor, mais preciso será o modelo.

                * **RMSE (Mean Absolute Percentage Error):** é a raiz quadrada do erro médio (MSE). \
                É uma medida que penaliza erros grandes de forma mais significativa do que erros menores, \
                proporcionando uma visão mais precisa da precisão do modelo. Quanto menor o valor do RMSE, \
                melhor o desempenho do modelo em relação aos dados de teste ou validação.

                * **MAPE (Mean Absolute Percentage Error):** O erro médio percentual absoluto é utilizado \
                para avaliar a precisão de um modelo de previsão em relação aos valores observados. É calculado \
                a partir da média das diferenças percentuais absolutas entre os valores previstos e os valores \
                reais. Quanto menor o MAPE, melhor será a precisão do modelo.
                """)
    st.markdown("<br>", unsafe_allow_html=True)

with tabs[3]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Insights das medidas de erros dos modelos]", anchor=False)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                Analisando as principais métricas de erro dos modelos como MSE(Mean Squared Error), \
                RMSE(Root Mean Squared Error) e MAPE(Mean Absolute Percentage Error), os resultados \
                apresentaram características bem distintas, se comparadas, mas devemos levar algumas \
                particularidades e escolhas de hiperparâmetros que fizemos em consideração:
                """)
    st.markdown("""            
                **1. A complexidade e capacidade de cada modelo**  
	                - LSTM: É uma variante das redes neurais recorrentes (RNN) e é particularmente \
                eficaz para capturar dependências de longo prazo e padrões complexos em séries temporais. \
                Ele pode se adaptar melhor às nuances dos dados de preço do petróleo, que podem incluir tendências \
                não lineares e efeitos de longo prazo.  
	                - Prophet: É um modelo aditivo adequado para séries temporais com fortes componentes \
                sazonais e tendências. Ele é projetado para ser fácil de usar e interpretar, mas pode não \
                capturar a mesma complexidade que um LSTM em dados altamente voláteis e não lineares.
                """)
    st.markdown("<br>", unsafe_allow_html=True)
