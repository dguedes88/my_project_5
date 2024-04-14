# Importar bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:/Users/User/Notebooks/my_project_5/vehicles.csv') # Lendo dados

# Criar um cabeçalho
st.header('Análise Exploratória de Dados')

# Criar um botão para criar um histograma
hist_button = st.button('Criar Histograma')

if hist_button: # Se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Adicionar outro botão para criar um gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button: # Se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x='odometer', y='price', title='Gráfico de Dispersão')
    st.plotly_chart(fig, use_container_width=True)