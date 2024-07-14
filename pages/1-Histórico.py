import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
        'Pandemia de COVID-19',
        'Conflito entre Rússia e Ucrânia'
    ],
    'DATA INÍCIO': [
        '1990-08-02',
        '1997-07-02',
        '2001-09-11',
        '2008-03-14',
        '2010-12-17',
        '2014-11-26',
        '2020-03-11',
        '2022-02-24'
    ]
}
df_eventos = pd.DataFrame(eventos)
df_eventos['DATA INÍCIO'] = pd.to_datetime(df_eventos['DATA INÍCIO'])




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
            petróleo "subiu" ou "desceu", normalmente é do preço do Brent que \
            se está falando. Devido a essa importância, sua cotação \
            serve de medida para decisões da OPEP (Organização dos \
            Países Exportadores de Petróleo) e outros países produtores.')
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader('O que influencia o preço do petróleo?', anchor=False)
st.markdown("""
            Apesar de hoje em dia, o Brasil ser um dos maiores produtores de petróleo ao redor do \
            mundo, a definição do preço no mercado nacional é bastante instável, uma vez que o preço \
            do barril é definido conforme reage o mercado internacional, sua cotação é em dólar, e \
            questões internacionais, desastres naturais, e crises políticas afetam diretamente o preço \
            dos combustíveis.  

            O mercado de petróleo é regularizado pela OPEP com a finalidade de manter estável a produção \
            desta commodity. Brasil, Estados Unidos e Rússia não fazem parte da OPEP, mas medidas \
            individuais podem driblar decisões da OPEP e mexer no mercado dos combustíveis. O órgão é composto \
            por: Angola, Arábia Saudita, Argélia, Emirados Árabes, Gabão, Guiné Equatorial, Irã, Iraque, \
            Kuwait, Líbia, Nigéria, República do Congo e Venezuela.  

            Quando falamos de desastres naturais, temos que terremotos, tsunamis e outros fenômenos \
            podem parar a produção local, a exemplo do Japão em 2011, onde um terremoto prejudicou as \
            refinarias JX Nippon Oil and Energy e Cosmo Oil, que foram atingidas por incêndios.  

            E, quando falamos de geopolítica, com a Guerra na Ucrânia, muitos países abdicaram a importação \
            de matérias primas oriundas da Rússia, com isso, outros produtores de petróleo precisaram \
            suprir a demanda, e aumentaram o preço do barril.
            """)
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
    yaxis=dict(range=[0, 160]),
    xaxis_title="Data",
    yaxis_title="Preço (US$)"
)
st.plotly_chart(fig)
st.markdown("<br><br>", unsafe_allow_html=True)





st.subheader('Relação entre os eventos históricos e o preço', anchor=False)

with st.expander(('Guerra do Golfo (1990)'), expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Guerra do Golfo]", anchor=False)
    st.markdown("""
                A Guerra do Golfo aconteceu entre 02 de agosto de 1990 e 28 de fevereiro de 1991 no \
                Oriente Médio. O conflito teve como motivação a invasão do Kuwait por tropas do Iraque, \
                sob o regime de Saddam Hussein, resultando em uma coalizão internacional com o intuito \
                de expulsar as tropas iraquianas.
                
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
        yaxis=dict(range=[0, 50]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    with col2: st.plotly_chart(fig_golfo)
    st.markdown("<br><br>", unsafe_allow_html=True)


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
    st.markdown("<br><br>", unsafe_allow_html=True)


with st.expander('Guerra ao Terror (2001)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Guerra ao Terror]", anchor=False)
    st.markdown("""
                Após sofrer com os atentados de 11 de setembro de 2001, os Estados Unidos \
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
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
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
    dados_terror = dados.loc[(dados['DATA'] >= '2000-07-01') & (dados['DATA'] <= '2008-06-30')].copy()
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
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    with col2: st.plotly_chart(fig_terror)
    st.markdown("<br><br>", unsafe_allow_html=True)


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
        st.markdown("<br><br>", unsafe_allow_html=True)
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
    st.markdown("<br><br>", unsafe_allow_html=True)


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
        st.markdown("<br><br>", unsafe_allow_html=True)
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
    st.markdown("<br><br>", unsafe_allow_html=True)


with st.expander('Alta oferta, baixa demanda (2014)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Período de alta oferta e baixa demanda]", anchor=False)
    st.markdown("""
                Este não é um evento, mas um período específico do mercado global de petróleo, \
                particularmente entre o final de 2014 e 2016. Durante esse tempo, a OPEP decidiu \
                não reduzir sua produção de petróleo, apesar da queda nos preços globais, \
                o que teve impactos significativos no mercado.

                As causas para a queda do valor do Brent foram um conjunto de fatores. Houve um aumento \
                significativo na produção de petróleo de xisto nos Estados Unidos, que contribuiu \
                para um excesso de oferta no mercado global. Outros países não membros da OPEP, como a \
                Rússia e o Canadá, também aumentaram sua produção, contribuindo para a oferta excessiva. \
                Ao mesmo tempo, a demanda global por petróleo não cresceu conforme o esperado devido \
                a uma desaceleração econômica em várias regiões, incluindo a China e a Europa.

                Em sua reunião de novembro de 2014, a OPEP, liderada pela Arábia Saudita, decidiu \
                manter sua produção inalterada, apesar da queda nos preços. A decisão foi vista \
                como uma tentativa de manter sua participação de mercado e pressionar os produtores \
                de petróleo de xisto nos EUA, cuja produção é mais cara. Nesse sentido, a estratégia \
                deu frutos, já que muitos desses produtores enfrentaram dificuldades financeiras e \
                foram forçados a reduzir ou fechar operações. Porém, os preços do petróleo Brent caíram \
                drasticamente, de cerca de US\$80 por barril em novembro de 2014 para menos de US\$30 \
                por barril no início de 2016. Por um lado, países cuja economia depende fortemente da \
                exportação de petróleo, como Venezuela, Nigéria e Rússia, enfrentaram graves dificuldades \
                econômicas devido à queda nos preços. Por outro, países consumidores se \
                beneficiaram dos preços mais baixos, o que ajudou a reduzir os custos de energia e \
                apoiar o crescimento econômico.

                Em novembro de 2016, a OPEP e vários países não membros, incluindo a Rússia, \
                concordaram em cortar a produção em cerca de 1,8 milhões de barris por dia. Esse \
                acordo foi estendido e mantido em várias reuniões subsequentes, ajudando a reduzir \
                o excesso de oferta no mercado global. A OPEP e seus aliados, conhecidos coletivamente \
                como OPEP+, continuaram a coordenar suas políticas de produção, estendendo os \
                cortes e adaptando suas estratégias conforme necessário para equilibrar o mercado.
                """
                )
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
                ##### Variação de preço no período

                À altura em que a OPEP tomou a decisão de não diminuir o ritmo de produção, o valor do \
                Brent já havia caído de cerca de US\$ 110 para US\$ 85. No início de 2015, abaixaria para \
                o patamar dos US\$ 45 e, após um ano de sobe-e-desce, chegaria a um fundo de US\$ 26 - \
                havia mais de 10 anos que o valor não chegava abaixo dos US\$ 30.

                O fim do período de interesse é pontuado pelo acordo de novembro de 2016, após o qual \
                os valores sobem com um pouco mais de força, retornando à faixa dos US\$ 50 em meados \
                de 2017.
                """)
    dados_ofdem = dados.loc[(dados['DATA'] >= '2013-01-01') & (dados['DATA'] <= '2018-07-31')].copy()
    dados_ofdem.reset_index(drop=True, inplace=True)
    dados_ofdem_hl = dados_ofdem.loc[(dados_ofdem['DATA'] >= '2014-11-01') & (dados_ofdem['DATA'] <= '2016-11-30')].copy()
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
    with col2: st.plotly_chart(fig_ofdem)
    st.markdown("<br><br>", unsafe_allow_html=True)


with st.expander('Pandemia de COVID-19 (2020)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Pandemia de COVID-19]", anchor=False)
    st.markdown("""
                A pandemia de COVID-19 teve um impacto dramático nos preços do petróleo \
                Brent devido a uma série de fatores que afetaram tanto a oferta quanto \
                a demanda no mercado global. A implementação de lockdowns e outras \
                restrições de mobilidade em todo o mundo para conter a disseminação \
                do vírus resultou em uma queda abrupta na demanda por petróleo. Viagens \
                aéreas, transporte terrestre e atividades industriais diminuíram drasticamente.

                No início de 2020, a falha em chegar a um acordo sobre cortes de produção \
                entre a OPEP e a Rússia levou a uma guerra de preços, com ambos os lados \
                aumentando a produção, exacerbando o excesso de oferta no mercado. A rápida \
                acumulação de estoques de petróleo devido à queda na demanda levou a \
                preocupações sobre a capacidade de armazenamento global, com tanques e \
                navios-tanque ficando lotados. Finalmente, em abril daquele ano, quando o \
                valor do Brent derreteu para a casa dos US\$9, chegou-se \
                a um acordo histórico para cortar a produção em aproximadamente 9,7 milhões \
                de barris por dia, na tentativa de equilibrar o mercado e apoiar os preços. \
                Este foi o maior corte de produção já acordado na história.

                Os lockdowns começaram a ser gradualmente levantados em diferentes momentos ao \
                redor do mundo, dependendo da situação específica de cada país e região em \
                relação ao controle da pandemia. Mas, de maneira geral, podemos dizer que o \
                relaxamento das restrições de contato social começou a acontecer entre maio \
                e agosto de 2020. E, com a aprovação e início da distribuição das vacinas \
                contra o COVID-19 no final daquele ano, muitos países começaram a planejar e \
                implementar uma reabertura mais ampla de suas economias no início de 2021. \
                A disponibilidade de vacinas foi, portanto, um fator chave para a \
                recuperação econômica e o aumento da demanda por petróleo.
                """
                )
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
                    ##### Variação de preço no período

                    A declaração de estado de pandemia foi feita em 11/03/2020, mas os preços já vinham \
                    despencando desde que notícias de casos da doença e de restrições radicais de mobilidade \
                    na China se espalhavam pelo mundo. Em 4 meses, de janeiro a abril de 2020, o valor foi de US\$ 70,25 \
                    para US\$ 9,12, o segundo menor valor histórico registrado nesta série temporal. Uma derrocada \
                    de 87%, maior que aquela registrada durante a crise financeira de 2008.  
                    A pandemia só viria a ter um fim "oficial" em maio de 2023, mas podemos observar que a \
                    retomada de alta dos preços acompanhou a retirada de medidas restritivas na metade de \
                    2020 e ganhou força após o início da vacinação, no começo do ano seguinte.
                    """)
    dados_pandemia = dados.loc[(dados['DATA'] >= '2019-01-01') & (dados['DATA'] <= '2021-12-31')].copy()
    dados_pandemia.reset_index(drop=True, inplace=True)
    dados_pandemia_hl = dados_pandemia.loc[(dados_pandemia['DATA'] >= '2020-01-01') & (dados_pandemia['DATA'] <= '2021-03-31')].copy()
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
        yaxis=dict(range=[0, 120]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    with col2: st.plotly_chart(fig_pandemia)
    st.markdown("<br><br>", unsafe_allow_html=True)


with st.expander('Conflito entre Rússia e Ucrânia (2022)', expanded=False):
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f":blue[Conflito entre Rússia e Ucrânia]", anchor=False)
    st.markdown("""
                Trata-se de um conflito atual entre Rússia e Ucrânia, ainda em andamento e sem \
                perspectiva de fim, que merece uma atenção especial. A \
                intenção de Putin era tomar a capital ucraniana, Kiev, mas as tropas russas foram \
                repelidas pelas ucranianas. Esta é uma guerra bastante sensível, pois de um lado passamos \
                a ter os Estados Unidos e a União Europeia como apoiadores da Ucrânia, fornecendo apoio \
                econômico, diplomático e militar a Kiev, enquanto China, Irã e Coreia do Norte apoiavam a Rússia.
                
                A participação da Rússia no setor de combustíveis fez com que a cotação do petróleo tivesse subido \
                ao patamar mais elevado desde a crise econômica de 2008. Em cerca de três semanas, o preço \
                cresceu mais de 20%. O petróleo representa mais da metade do volume de negociação das mercadorias \
                e é a principal matriz energética do mundo, com isso a Rússia é responsável por 12% da produção \
                global de óleo e gás e, além disso, é o principal exportador mundial de petróleo e produtos \
                petrolíferos combinados. Grande parte da produção é destinada à UE, o que fragiliza uma \
                resposta mais enfática desses países contra o presidente russo Vladimir Putin, especialmente \
                em meio a um inverno rigoroso, em que os europeus dependem do gás russo para a calefação.
                """)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
                    ##### Variação de preço no período

                    O preço saltou mais de 20% em 3 semanas, provocando problemas em inúmeras economias, \
                    pois além de ocasionar o aumento no petróleo, outras atividades econômicas foram \
                    impactadas, como a importação de arroz, grãos, óleo, gás, remédios, entre outros.
                    """)
    dados_ucrania = dados.loc[(dados['DATA'] >= '2021-07-01') & (dados['DATA'] <= '2023-12-31')].copy()
    dados_ucrania.reset_index(drop=True, inplace=True)
    dados_ucrania_hl = dados_ucrania.loc[(dados_ucrania['DATA'] >= '2022-02-24') & (dados_ucrania['DATA'] <= '2023-02-28')].copy()
    dados_ucrania_hl.reset_index(drop=True, inplace=True)
    fig_ucrania = go.Figure()
    fig_ucrania.add_trace(go.Scatter(
        x=dados_ucrania['DATA'],
        y=dados_ucrania['PREÇO'],
        mode='lines',
        name='Preço'))  
    fig_ucrania.add_trace(go.Scatter(
        x=dados_ucrania_hl['DATA'],
        y=dados_ucrania_hl['PREÇO'],
        mode='lines',
        name='Período de interesse',
        line=dict(color='red')))
    fig_ucrania.update_layout(
        yaxis=dict(range=[0, 150]),
        xaxis_title='Data',
        yaxis_title='Preço (US$)')
    with col2: st.plotly_chart(fig_ucrania)
    st.markdown("<br><br>", unsafe_allow_html=True)
