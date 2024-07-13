import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Carregar os dados
previsao_prophet = pd.read_csv('previsao_prophet.csv', sep=',') #depois mudar pro caminho do git
previsao_prophet['ds'] = pd.to_datetime(previsao_prophet['ds'])  # Converter a coluna 'ds' para datetime
previsao_prophet['trend'] = round(previsao_prophet['trend'],2)
previsao_prophet = previsao_prophet.rename(columns={'ds':'data','trend':'previsao_$'})
previsao_prophet = previsao_prophet.query("data > '2024-06-20'")

previsao_lstm = pd.read_csv('previsao_lstm.csv', sep=',') #depois mudar pro caminho do git
previsao_lstm['ds'] = pd.to_datetime(previsao_lstm['ds'])  # Converter a coluna 'ds' para datetime
previsao_lstm['previsao'] = round(previsao_lstm['previsao'],2)
previsao_lstm = previsao_lstm.rename(columns={'ds':'data','previsao':'previsao_$'})
previsao_lstm = previsao_lstm.query("data > '2024-06-20'")

########################### STREAMLIT ##########################
st.title('Previsão do Preço do Barril de Petróleo Brent')

# Definindo as abas
tabs = st.tabs(["Previsão com o Prophet", "Previsão com o LSTM"])

# Conteúdo da Aba 1
with tabs[0]:
    # Data inicial fixa
    start_date = datetime(2024, 6, 21)

    # Data final padrão
    end_date_default = datetime(2024, 7, 20)
    max_date = end_date_default

    # Criar o campo de seleção de data para a data final
    end_date = st.slider(
        'Selecione a data final da previsão (data mínima 21/06/2024 e data máxima 20/07/2024):',
        min_value=start_date,
        max_value=end_date_default,
        value=start_date,
        format="YYYY-MM-DD",
        key='slider1'
    )

    # Mostrar as datas selecionadas
    st.write(f'Data inicial fixa de previsão: {start_date.date()}')
    st.write(f'Data final da previsão: {end_date.date()}')


    def consultar_eventos(end_date):
        if end_date == max_date:
            # Se a data final for a máxima, mostrar toda a tabela
            resultados = previsao_prophet
        else:
            # Caso contrário, mostrar a consulta com as datas especificadas
            resultados = previsao_prophet[(previsao_prophet['data'] >= start_date) & (previsao_prophet['data'] <= end_date)]
        return resultados



    if st.button('Buscar Previsão', key='button1'):
        # Realizar a consulta e obter os resultados
        resultados = consultar_eventos(end_date)

        # Mostrar os resultados
        if not resultados.empty:
            st.write("Eventos até a data final informada:")
            # Converter o DataFrame para HTML sem o índice
            st.write(resultados.to_html(index=False), unsafe_allow_html=True)
        else:
            st.write("Não há eventos até a data final informada.")

# Conteúdo da Aba 2
with tabs[1]:
    # Data inicial fixa
    start_date2 = datetime(2024, 6, 21)

    # Data final padrão
    end_date_default2 = datetime(2024, 7, 20)
    max_date2 = end_date_default2

    # Criar o campo de seleção de data para a data final
    end_date2 = st.slider(
        'Selecione a data final da previsão (data mínima 21/06/2024 e data máxima 20/07/2024):',
        min_value=start_date2,
        max_value=end_date_default2,
        value=start_date2,
        format="YYYY-MM-DD",
        key='slider2'
    )

    # Mostrar as datas selecionadas
    st.write(f'Data inicial fixa de previsão: {start_date2.date()}')
    st.write(f'Data final da previsão: {end_date2.date()}')


    def consultar_eventos2(end_date2):
        if end_date2 == max_date2:
            # Se a data final for a máxima, mostrar toda a tabela
            resultados2 = previsao_lstm
        else:
            # Caso contrário, mostrar a consulta com as datas especificadas
            resultados2 = previsao_lstm[(previsao_lstm['data'] >= start_date2) & (previsao_lstm['data'] <= end_date2)]
        return resultados2



    if st.button('Buscar Previsão', key='button2'):
        # Realizar a consulta e obter os resultados
        resultados2 = consultar_eventos2(end_date2)

        # Mostrar os resultados
        if not resultados2.empty:
            st.write("Eventos até a data final informada:")
            # Converter o DataFrame para HTML sem o índice
            st.write(resultados2.to_html(index=False), unsafe_allow_html=True)
        else:
            st.write("Não há eventos até a data final informada.")

