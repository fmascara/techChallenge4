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

## INÍCIO DA VISUALIZAÇÃO:
st.subheader(":red[Tech Challenge Fase 4]", divider="red", anchor=False)
st.markdown("<br>", unsafe_allow_html=True)
st.subheader('Insights sobre a variação do preço do petróleo', anchor=False)
st.write('Ao longo do desenvolvimento deste estudo, podemos destacar alguns insights \
         relacionados a variação do preço do petróleo.')
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 1. Conflitos regionais")
st.markdown("""
            Notamos que, ao logo do período histórico analisado, tivemos conflitos geopolíticos \
            e guerras que afetaram em larga escala a produção e preços do combustível, onde na \
            maioria das vezes, foram situações concentradas entre países do oriente médio, onde \
            eles detêm a maior parte da produção mundial de petróleo. A começar pela Guerra do Golfo \
            em 1990, que envolveu uma invasão territorial do Iraque em cima de Kuwait, havendo \
            conflito de interesses, uma vez que, Kuwait estava promovendo a super extração de petróleo, \
            gerando assim uma queda no preço do combustível, e com isso, prejudicava diretamente a \
            economia iraquiana.
            
            Em 20 de março de 2003, as forças americanas e aliadas invadiram o Iraque e derrubaram o \
            regime de Saddam Hussein. Os EUA disseram que o Iraque tinha armas de destruição em massa e \
            era uma ameaça à paz internacional. [7] Com isso, gerou-se uma preocupação alarmante, pois \
            como o Oriente Médio detinha grande parte da produção de petróleo, o abastecimento mundial \
            ficou comprometido, tendo a necessidade de aumentar os preços de petróleo advindos de outros produtores.
            
            E, destacamos também as turbulências na Primavera Árabe, que foi marcada pela insatisfação \
            popular com relação aos regimes autoritários, desigualdade econômica, corrupção e restrições políticas.
            
            **Conclusão:** Quanto mais desavenças, conflitos e guerras houver, podemos ter queda na produção de \
            petróleo e com isso, gerar aumentos significativos para quem estiver demandando.
            """)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 2. Papel da OPEP")
st.markdown("""
            O órgão OPEP (Organização dos Países Exportadores de Petróleo) criado em 1960 no Iraque, tem \
            como objetivo proteger e estabelecer uma política comum em relação à produção e à venda de \
            petróleo, a fim de não gerar descolamento de produção e preço entre os países membros. É \
            responsável por intervir com a produção de concorrentes externos que estejam afetando diretamente \
            os produtores da OPEP, e define os momentos adequados para aumentar ou reduzir a produção, bem \
            como regular as novas tecnologias que podem contribuir dentro do mercado.
            
            Ou seja, é um importante órgão que busca garantir a presença da commodity, e manter o mercado em equilíbrio.
            
            **Conclusão:** A OPEP tem o poder de controlar a oferta de petróleo, e com isso, ser um dos principais \
            responsáveis em definir qual será o preço de mercado (internacional), que esta commodity poderá ser oferecida.
            """)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 3. Crises econômicas globais")
st.markdown("""
            Destacamos a crise econômica de 2008 e a Grande Recessão em 2009. A crise originou-se nos Estados Unidos \
            dentro do mercado imobiliário, mas rapidamente afetou diversos outros setores e externalizou a nível \
            mundial. Tudo começou com uma crise no setor imobiliário americano, onde muitos empréstimos hipotecários \
            de alto risco foram concedidos a pessoas que não tinham condições de honrar com os compromissos. Logo, \
            começaram a inadimplir e houve uma queda abrupta nos preços dos imóveis. Muitos bancos e instituições \
            financeiras tinham ativos ligados a estes ativos do mercado imobiliário, com isso, aumentaram as crises, \
            gerou-se perdas e falências em bancos de investimentos e seguradoras.
            
            A crise espalhou-se globalmente, tanto para países desenvolvidos quanto emergentes, promovendo uma \
            desaceleração econômica. A recessão afetou em maior escala os EUA e Europa, onde diminuiu o consumo, \
            investimento e comércio internacional.
            
            Com isso, o preço do barril chegou a rondar os 140 dólares por barril, e em meses, tivemos uma queda \
            livre do seu preço até o nível dos 40 dólares por barril. A redução na demanda global combinada com \
            preocupações sobre o crescimento econômico levou a esta queda abrupta no preço do petróleo.
            
            **Conclusão:** Devido a toda crise econômica, o mercado se viu em um momento extremamente especulativo e \
            volátil, ou seja, crises financeiras interferem diretamente de como caminhará a sensibilidade de \
            mercado em relação a oferta e demanda. Assuntos de nível global, interferem inúmeras economias, e f\
            alando-se de petróleo, ele é responsável e necessário para o funcionamento logístico de diversos setores.
            """)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 4. Energia e sustentabilidade")
st.markdown("""
            Muito se fala ao redor do mundo, a respeito de novas fontes de energia, sendo sempre abordado as \
            Fontes de Energias Renováveis , como a hídrica (energia da água dos rios), solar (energia do sol), \
            eólica (energia do vento), biomassa (energia de matéria orgânica), geotérmica (energia do interior \
            da Terra) e oceânica (energia das marés e das ondas) [9], com isso, a energia advinda de combustíveis \
            tende a diminuir  ao decorrer do tempo, promovendo uma menor demanda dos produtores. Além do que, \
            são mudanças que afetam positivamente a sustentabilidade mundial.
            
            **Conclusão:** Quanto mais alternativas renováveis e sustentáveis surgir no mercado, passaremos \
            ter um mercado mais competitivo, com maiores opções de  produção de energia, logo  o preço do petróleo \
            tenderá a diminuir, caso a OPEP não reduza o volume produzido desta commodity. 
            """)

