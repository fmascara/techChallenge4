import streamlit as st
from utils.resources import custom_sidebar, config_pagina

config_pagina()

## VISUALIZAÇÃO:
custom_sidebar()

st.subheader(":red[Tech Challenge Fase 4]", divider="red", anchor=False)

st.title('Estudos sobre o preço do petróleo tipo Brent', anchor=False)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Sobre este trabalho', anchor=False)
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
with st.container(border=True):
    st.markdown("""
                <strong>Os arquivos usados na construção deste app, bem como o notebook Jupyter onde \
                foram construídas as previsões, podem ser encontrados \
                <a href="https://github.com/fmascara/techChallenge4">neste repositório</a> do GitHub.</strong>
                """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Fontes dos dados', anchor=False)
st.write('Os preços para este estudo foram obtidos no site\
            do IPEA, mas são provenientes originalmente da EIA.')
st.markdown('<a href="https://www.ipea.gov.br/portal/coluna-3/institucional-sep/quem-somos">\
            IPEA - Instituto de Pesquisa Econômica Aplicada</a> - \
            é uma fundação pública federal vinculada ao Ministério \
            da Economia. Suas atividades de pesquisa fornecem suporte \
            técnico e institucional às ações governamentais para a \
            formulação e reformulação de políticas públicas e programas \
            de desenvolvimento brasileiros. O Ipea é responsável pelo \
            levantamento e divulgação de dados econômicos do Brasil, \
            e seu trabalho serve de base para ações governamentais em diversas áreas.', unsafe_allow_html=True)
st.markdown('<a href="https://economiaenegocios.com/administracao-de-informacoes-de-energia-eia/">\
            EIA - Energy Information Administration</a> - é uma agência \
            governamental dos Estados Unidos formada em 1977. Sua missão \
            é coletar, analisar e disseminar informações independentes \
            e imparciais sobre energia, promovendo a formulação de \
            políticas sólidas, mercados eficientes e compreensão pública \
            sobre a energia e sua interação com a economia e o meio ambiente.', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Referências', anchor=False)
st.markdown("#### Histórico e eventos:", unsafe_allow_html=True)
st.write('https://br.investing.com/analysis/petroleo-brent-entendendo-o-mercado-e-seus-impactos-200463965, \
         "Petróleo Brent: Entendendo o mercado e seus impactos"')
st.write('https://blog.toroinvestimentos.com.br/trading/petroleo-brent-wti/, "Petróleo tipo Brent x WTI"')
st.write('https://www.politize.com.br/guerra-do-golfo/, "Saiba o que foi a Guerra do Golfo"')
st.write('https://mundoeducacao.uol.com.br/historiageral/guerra-iraque.htm, "Guerra do Iraque"')
st.write('https://diplomatique.org.br/vinte-anos-da-guerra-ao-terror/, "Vinte anos da Guerra ao Terror"')
st.write('https://g1.globo.com/Noticias/Economia_Negocios/0,,MUL940136-9356,00-O+ANO+EM+QUE+O+PETROLEO+ENLOUQUECEU+O+MERCADO.html, \
         "2008, o ano em que o petróleo enlouqueceu o mercado"')
st.write('https://www.bbc.com/portuguese/internacional-55379502, "O que foi e como terminou a Primavera Árabe?"')
st.write('https://www.todamateria.com.br/primavera-arabe/, "Primavera Árabe"')
st.write('https://exame.com/economia/precos-do-petroleo-se-aproximam-do-fundo-do-poco-de-2008/, \
         "Preços do petróleo se aproximam do fundo do poço de 2008"')
st.write('https://economia.uol.com.br/noticias/afp/2014/11/27/opep-mantem-teto-de-producao-inalterado.htm, \
         "OPEP mantém teto de produção inalterado"')
st.write('https://g1.globo.com/economia/noticia/2015/01/entenda-queda-do-preco-do-petroleo-e-seus-efeitos.html, \
         "Entenda a queda do preço do petróleo e seus efeitos"')
st.write('https://www.ibp.org.br/observatorio-do-setor/analises/covid-19-e-os-impactos-sobre-o-mercado-de-petroleo/, "COVID-19 e os impactos no preço do petróleo"')
st.write('https://www.bbc.com/portuguese/internacional-58934505, "Por que o preço do petróleo está disparando no mundo todo?"')

st.write('https://www.estadao.com.br/internacional/dois-anos-de-guerra-na-ucrania-quando-comecou-quem-esta-ganhando-e-o-que-pode-acontecer-no-futuro-nprei/, "Dois anos de guerra na Ucrânia"')
st.write('https://www.epe.gov.br/pt/abcdenergia/fontes-de-energia#, "Fontes de Energia"')
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### Bibliotecas e modelos:", unsafe_allow_html=True)
st.write('https://streamlit.io/, "Documentação do Streamlit"')
st.write('https://facebook.github.io/prophet/docs/quick_start.html, "Documentação do Prophet"')
st.write('https://keras.io/api/layers/recurrent_layers/lstm/, "Documentação do Keras LSTM"')
st.write('https://www.alura.com.br/artigos/metricas-de-avaliacao-para-series-temporais, "Métricas para avaliação de séries temporais"')
