import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static

dados = {
         'Municipio': ['São Luís', 'São José de Ribamar', 'Paço do Lumiar', 'Raposa'],
         '2016': [1200, 500, 300, 150],
         '2017': [1300, 550, 350, 200],
         '2018': [1400, 600, 400, 250],
         '2019': [1500, 650, 450, 300],
         '2020': [1600, 700, 500, 350]
}
df = pd.DataFrame(dados)
df = df.set_index('Municipio')

st.title('Dashboard de Saúde Pública - Grande São Luís')
st.write('Análise da Incidência de Doenças Respiratórias (2016-2020)')

# Seleção de Município
municipio = st.selectbox('Selecione o Município', df.index)

# Gráfico de Linhas
st.subheader(f'Incidência de Doenças Respiratórias em {municipio}')

fig, ax = plt.subplots()
ax.plot(df.columns, df.loc[municipio], marker='o')

ax.set_title(f'Incidência de Doenças Respiratórias em {municipio}')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de Casos')

st.pyplot(fig)

# Gráfico de Barras Comparativo
st.subheader('Comparação entre Municípios')

ano = st.selectbox('Selecione o Ano', df.columns)

fig, ax = plt.subplots()
sns.barplot(x=df.index, y=df[ano], ax=ax)

ax.set_title(f'Incidência de Doenças Respiratórias em {ano}')
ax.set_xlabel('Município')
ax.set_ylabel('Número de Casos')

plt.xticks(rotation=45)

st.pyplot(fig)

# Mapa Geoespacial
st.subheader('Mapa Geoespacial da Incidência de Doenças Respiratórias')
coordenadas = {
    'São Luís': [-2.53874, -44.2825],
    'São José de Ribamar': [-2.56194, -44.0519],
    'Paço do Lumiar': [-2.516, -44.1014],
    'Raposa': [-2.4254, -44.0972]
}

mapa = folium.Map(location=[-2.53874, -44.2825], zoom_start=11)
for municipio, casos in zip(df.index, df[ano]):
    folium.Marker(
        location=coordenadas[municipio],
        popup=f'{municipio}: {casos} casos',
        icon=folium.Icon(color='red' if casos > 1000 else 'green')
    ).add_to(mapa)

folium_static(mapa)

