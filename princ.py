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
