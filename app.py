import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("data/vehicles_us.csv")

st.header('Análisis Exploratorio de Datos : Vehículos Usados ')

#OBJETO 1: boton/casilla de verificación- gráfica
#hist_button = st.button('Construir histograma')
#if hist_button:
#   st.write('Histograma para el conjunto de datos de venta de vehículos usados')
#    fig = px.histogram(car_data, x="odometer", title='Distribución del kilometraje')
#    st.plotly_chart(fig, use_container_width=True)

#OBJETO 2: boton- gráfica
#scatter_button = st.button('Construir gráfico de dispersión') 
#if scatter_button:
#    st.write('Gráfico de dispersión para el conjunto de datos de venta de vehículos usados')
#    fig = px.scatter(car_data, x="odometer", y="price", title='Relación entre kilometraje y precio') 
#    st.plotly_chart(fig, use_container_width=True)

#OBJETO 1: casilla de verificación- gráfica
#build_histogram = st.checkbox('Construir histograma')
#if build_histogram:
#    st.write('Histograma para el conjunto de datos de venta de vehículos usados')
#    fig = px.histogram(car_data, x="odometer", title='Distribución del kilometraje')
#    st.plotly_chart(fig, use_container_width=True)

#OBJETO 2: casilla de verificación- gráfica
#build_scatter = st.checkbox('Construir gráfico de dispersión')
#if build_scatter:
#    st.write('Gráfico de dispersión para el conjunto de datos de venta de vehículos usados')
#    fig = px.scatter(car_data, x="odometer", y="price", title='Relación entre kilometraje y precio') 
#    st.plotly_chart(fig, use_container_width=True)

# Lista de opciones para checkboxes
options = st.multiselect("Selecciona las gráficas que quieres mostrar:",
                         ["Histograma", "Gráfico de dispersión",'Gráfico de barras','Gráfico de Pastel(piechart)',
                          'Gráfico de Lineas','Gráfico de Caja(boxplot)'])

# Mostrar las gráficas seleccionadas
if "Histograma" in options:
    st.write('Histograma para el conjunto de datos de venta de vehículos usados')
    fig_hist = px.histogram(car_data, x="odometer", title='Distribución del kilometraje')
    st.plotly_chart(fig_hist, use_container_width=True)

if "Gráfico de dispersión" in options:
    st.write('Gráfico de dispersión para el conjunto de datos de venta de vehículos usados')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title='Relación entre kilometraje y precio') 
    st.plotly_chart(fig_scatter, use_container_width=True)

if 'G´rafico de barras' in options:
    st.write ('Gráfico de barras para el conjunto de datos de venta de vehículos usados')
    price_type = car_data.groupby("type")["price"].mean().reset_index()
    fig_bar = px.bar(price_type, x="price", y="type", orientation='h',title= 'Tipo de carro y precio promedio')
    st.plotly_chart(fig_bar,use_container_width=True)

    price_condition = (car_data.groupby("condition")["price"].mean().reset_index())
    fig_bar2 = px.bar(price_condition,x="price",y="condition",orientation="h",title='Estado del vehiculo y su precio')
    st.plotly_chart(fig_bar2,use_container_width=True)

if 'Gráfico de Pastel(piechart)' in options:
    st.write("Gráfico de pastel para el conjunto de datos de venta de vehículos usados")
    fig_pie = px.pie(car_data,names="type",title="Distribución de vehículos por tipo",hole=0.3) 
    st.plotly_chart(fig_pie, use_container_width=True)

if 'Gráfico de Lineas' in options: 
    st.write("Gráfico de línea para el conjunto de datos de venta de vehículos usados")
    price_by_year = car_data.groupby("model_year")["price"].mean().reset_index()
    fig_line = px.line(price_by_year, x="model_year",y="price",title="Evolución del precio promedio según el año del modelo")
    st.plotly_chart(fig_line, use_container_width=True)

if  'Gráfico de Caja(boxplot)' in options:
    st.write("Gráfico de caja para el conjunto de datos de venta de vehículos usados")
    fig_box = px.box(car_data,x="transmission",y="price",color="transmission",title="Distribución de precios según tipo de transmisión")
    st.plotly_chart(fig_box, use_container_width=True)
    