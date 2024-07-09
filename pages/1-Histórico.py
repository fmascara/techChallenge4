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
                As causas do conflito guardam relação estreita com o petróleo. Após a longa \
                e custosa Guerra Irã-Iraque \
                (1980-1988), o Iraque estava profundamente endividado, principalmente com o \
                Kuwait e a Arábia Saudita. O Iraque acusava o Kuwait de roubar petróleo da reserva \
                de Rumaila, que se estendia pela fronteira entre os dois países. Alegava também que \
                o país vizinho estava excedendo suas quotas de produção \
                estabelecidas pela OPEP, contribuindo para a queda dos preços do petróleo, o que \
                prejudicava a economia iraquiana.
                Portanto, a invasão do Kuwait pelo Iraque foi, em parte, \
                motivada pelo desejo de Saddam Hussein de controlar as vastas reservas de petróleo \
                do Kuwait, que eram uma das maiores do mundo. O controle sobre essas reservas \
                fortaleceria significativamente a posição econômica e política do Iraque.

                Durante o conflito, houve volatilidade nos preços,\
                que aumentaram com o início da guerra e voltaram a cair após a rápida vitória da coalizão \
                e a segurança relativa do fornecimento de petróleo. Após a guerra, o Iraque \
                enfrentou severas sanções econômicas \
                impostas pelas Nações Unidas, que incluíam restrições à exportação de petróleo. Estas \
                sanções tiveram um impacto devastador na economia iraquiana.
                
                A guerra destacou a importância da estabilidade no mercado \
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
                pelas tropas lideradas pelos EUA. 
                Durante o período de guerra, o preço passou a barreira dos US\$40 pela primeira \
                vez nessa série histórica. Após o término do conflito, o preço voltou a \
                patamares próximos do que era antes (em torno dos US\$20).
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
                entra em uma evidente queda. Nesse período o preço atingiu o seu valor mínimo histórico, \
                US$ 9,10 em 10/12/1998. 
                No meio dessa descida, ocorrem os dois acordos da OPEP \
                (jul/1998 e mar/1999) para cortar a produção e tentar conter a derrocada. A data de 31/03/1999 \
                marca o fim do período de interesse, após o qual vemos uma forte ascensão do preço do \
                petróleo, para patamares acima daqueles observados no período anterior à crise.
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
    st.markdown("""
                'Após sofrer com os atentados de 11 de setembro de 2001, os Estados Unidos \
                decidiram empreender uma “guerra contra o terror” apontando os governos que \
                poderiam representar riscos à paz mundial. Nesse sentido, o presidente norte-americano \
                George W. Bush e seu Conselho de Estado passaram a fazer uma campanha política \
                pregando a intervenção no chamado “eixo do mal”. Entre os países que compunham esse \
                grupo, estariam o Afeganistão, berço da Al-Qaeda - grupo responsável por \
                coordenar os ataques - e o Iraque, ainda liderado pelo ditador Saddam Hussein.\
                O mundo todo, entretanto, questionava se as razões invocadas pelo governo \
                norte-americano para a empreitada - eliminar armas de destruição em massa, combater o \
                terrorismo, prevenir ameaças contra Estados vizinhos, derrubar a ditadura de \
                Saddam Hussein - não se prestavam unicamente a encobrir um evidente interesse nas \
                reservas de petróleo iraquianas, uma das maiores do mundo. 

                A invasão do Afeganistão em outubro de 2002 e, principalmente, do Iraque em março de 2003 \
                causaram uma elevação nos preços do petróleo, após a queda inicial que seguiu-se aos atos terroristas. \
                A incerteza sobre a continuidade da produção iraquiana e a possibilidade de danos à infraestrutura \
                petrolífera levaram a essa alta. A Guerra ao Terror também teve efeitos de longo prazo no \
                mercado de petróleo ao influenciar os investimentos em exploração e produção. \
                A instabilidade na região do Oriente Médio fez com que as empresas petrolíferas reconsiderassem \
                investimentos e aumentassem os custos de segurança. Isso, combinado com a percepção de risco \
                geopolítico elevado, contribuiu para a manutenção de preços mais altos.
                """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                ##### Variação de preço no período

                A Guerra ao Terror teve um impacto combinado significativo no mercado de petróleo, \
                influenciando tanto a oferta quanto a demanda, além de adicionar \
                uma camada de risco geopolítico que afetou os preços do petróleo a longo prazo.

                Imediatamente após os atentados, vemos uma curva decrescente no preço. Normalmente, \
                a incerteza quanto ao abastecimento de um produto tão essencial leva a altas nos preços, \
                mas os atentados causaram uma queda generalizada no mercado financeiro. Por exemplo, a \
                Bolsa de NY permaneceu fechada por vários dias e, quando reabriu, sofreu uma das maiores \
                quedas da sua história. O medo inicial pode ter levado investidores a vender por pânico \
                e reavaliar seus portifólios buscando ativos mais seguros, pressionando os preços do \
                petróleo para baixo.

                Enquanto os Estados Unidos se preparavam para a invasão do Afeganistão, em out/2001, \
                e do Iraque, em mar/2002, os preços voltaram a subir. No entanto, a Guerra do Iraque durou \
                mais de 7 anos (2003 a 2011); a instabilidade causada no mercado nesse período elevou \
                os preços para patamares nunca atingidos antes. A barreira dos US\$50 foi ultrapassada pela \
                primeira vez em out/2004, e a dos US\$100 em mar/2008.
                """)
    dados_terror = dados.loc[(dados['DATA'] >= '2000-07-01') & (dados['DATA'] <= '2008-07-31')].copy()
    dados_terror.reset_index(drop=True, inplace=True)
    dados_terror_hl = dados_terror.loc[(dados_terror['DATA'] >= '2001-09-11') & (dados_terror['DATA'] <= '2006-12-31')].copy()
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
    st.markdown("""
                Antes da crise, o crescimento econômico robusto em economias emergentes como \
                China e Índia aumentou significativamente a demanda por petróleo. O crescimento \
                industrial e a expansão da infraestrutura nesses países aumentaram o \
                consumo de energia. Nos Estados Unidos e em outros países desenvolvidos, \
                o consumo de combustíveis continuava alto, contribuindo para a pressão sobre \
                a demanda global por petróleo. Por outro lado, a ocupação norte-americana no Iraque e novos conflitos que \
                ocorriam no Oriente Médio ameaçavam a segurança das rotas de fornecimento \
                de petróleo e aumentavam o risco geopolítico, elevando os preços.

                Além disso, com a percepção de petróleo e outras commodities como um hedge (proteção) contra a \
                inflação e a depreciação do dólar, houve um aumento significativo na especulação \
                financeira no mercado de futuros de petróleo. Investidores buscavam ganhos com a alta \
                dos preços, alimentando ainda mais a escalada.

                Com o colapso do Lehman Brothers em setembro de 2008, desencadeou-se a crise, que levou \
                a uma recessão econômica global. A desaceleração econômica reduziu drasticamente a \
                demanda por petróleo, especialmente nos setores de transporte e indústria. A recessão \
                nos Estados Unidos, Europa e outras economias desenvolvidas resultou em uma queda \
                abrupta no consumo de petróleo, contribuindo para a queda dos preços.

                Com a queda na demanda, os estoques de petróleo aumentaram. Os países \
                começaram a acumular estoques, exacerbando o desequilíbrio entre oferta e demanda. A \
                OPEP tentou responder à queda dos preços com cortes na produção, mas essas \
                medidas levaram tempo para ter efeito e estabilizar o mercado.

                No mercado financeiro, com o cenário se invertendo, os investidores buscaram \
                liquidez e venderam seus  ativos, incluindo contratos futuros de petróleo. A venda \
                em massa pressionou ainda mais os preços para baixo.
                """
                )
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("""
                ##### Variação de preço no período

                A crise financeira global de 2008 causou uma volatilidade extrema nos preços do \
                petróleo e uma variação bastante notável: queda de 77% em três meses. \
                A alta histórica de cerca de US\$143 por barril em julho de 2008 foi \
                impulsionada por um forte crescimento da demanda, restrições na oferta e \
                especulação no mercado. A subsequente queda acentuada para cerca de US\$33 por \
                barril em dezembro do mesmo ano foi resultado da queda na demanda devido à \
                recessão global, liquidação de ativos por parte dos investidores, aumento dos \
                estoques e apreciação do dólar. A crise financeira mostrou como os mercados de \
                petróleo são sensíveis a mudanças econômicas globais e a eventos financeiros imprevistos.
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
    with col2: st.plotly_chart(fig_crise)


with st.expander('Primavera Árabe (2010)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Primavera Árabe]", anchor=False)
    st.markdown("""
                A Primavera Árabe foi uma série de protestos, revoluções e levantes que se espalharam pelo \
                mundo árabe a partir de dezembro de 2010, resultando em mudanças políticas significativas \
                em vários países. Esse período de instabilidade teve um impacto direto nos preços do petróleo \
                Brent, dada a importância da região do Oriente Médio e do Norte da África para a produção \
                global de petróleo.
                """)
    st.markdown('**Principais Marcos e Movimentos**')
    st.markdown("""
                * Tunísia (Dezembro 2010 - Janeiro 2011):
                    - Início dos Protestos: A imolação de Mohamed Bouazizi, um vendedor de rua, em dezembro \
                de 2010 desencadeou protestos massivos contra o governo. Em janeiro de 2011, o presidente \
                Zine El Abidine Ben Ali foi deposto.
                    - Impacto no Petróleo: Embora a Tunísia não seja um grande produtor, o \
                sucesso inicial dos protestos inspirou movimentos em outros países, aumentando a incerteza \
                regional.
                """)
    st.markdown("""
                * Egito (Janeiro - Fevereiro 2011):
                    - Protestos na Praça Tahrir: Manifestações massivas levaram à queda do presidente Hosni \
                Mubarak em fevereiro de 2011, após 30 anos no poder.
                    - Impacto no Petróleo: O Egito controla o Canal de Suez e o Oleoduto SUMED, rotas \
                críticas para o transporte de petróleo. A instabilidade levantou preocupações sobre possíveis \
                interrupções no seu trânsito.
                """)
    st.markdown("""
                * Líbia (Fevereiro - Outubro 2011):
                    - Guerra Civil: Protestos contra o regime de Muammar Gaddafi evoluíram \
                para uma guerra civil. Em outubro de 2011, Gaddafi foi capturado e morto.
                    - Impacto no Petróleo: A Líbia, um grande produtor, viu sua produção cair \
                drasticamente durante a guerra civil, afetando significativamente os preços globais.
                """)
    st.markdown("""
                * Síria (Março 2011 - Presente):
                    - Guerra Civil: Protestos contra o presidente Bashar al-Assad evoluíram para \
                uma prolongada guerra civil, ainda em andamento.
                    - Impacto no Petróleo: Embora a produção de petróleo da Síria não seja grande \
                em termos globais, a guerra civil contribuiu para a instabilidade regional.
                """)
    st.markdown("""
                * Bahrein (Fevereiro - Março 2011):
                    - Protestos e Repressão: Protestos liderados pela maioria xiita contra a monarquia \
                sunita foram fortemente reprimidos.
                    - Impacto no Petróleo: Bahrein não é um grande produtor, mas a repressão dos \
                protestos teve apoio de outros países do Golfo, destacando a preocupação regional com a estabilidade.
                """)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("""
                ##### Variação de preço no período

                A instabilidade política, econômica e social em várias nações produtoras de petróleo aumentaram a \
                incerteza sobre a oferta, levando a uma alta nos preços do Brent. Em 2011, \
                o preço do petróleo - que, com a estabilização da crise após 2009, vinha se mantendo \
                na faixa entre US\$70 e US\$80 - voltou a cruzar a marca dos US\$100 por barril. A incerteza \
                sobre a continuidade da produção e do transporte de petróleo na região, juntamente com o \
                risco geopolítico elevado, contribuiu para a alta volatilidade e o aumento dos preços do \
                durante este período e uma grande oscilação (normalmente acima dos US\$100) nos 3 anos seguintes.
                """)
    dados_prim = dados.loc[(dados['DATA'] >= '2009-07-01') & (dados['DATA'] <= '2014-07-31')].copy()
    dados_prim.reset_index(drop=True, inplace=True)
    dados_prim_hl = dados_prim.loc[(dados_prim['DATA'] >= '2010-12-17') & (dados_prim['DATA'] <= '2011-12-31')].copy()
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
    with col2: st.plotly_chart(fig_prim)


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
