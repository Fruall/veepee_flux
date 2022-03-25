import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
from tqdm import tqdm, tqdm_notebook

st.header("Veepee Flux")


df = pd.read_csv('veepee_catalog_final.csv', sep=';', encoding='utf-8')
#df = pd.read_excel('veepee_catalog_final.xlsx')

#df = pd.read_excel('veepee_catalog_final.xlsx', engine='openpyxl')

df = df[['Title', 'Label', 'Univers']]

total_products = df['Title'].count()
duplicated_titles = round((df['Title'].count() - df['Title'].nunique()) / df['Title'].count(), 2)
labelled_products = 100 - round((df['Label'].isna()).sum()/(df['Title'].count()),2) * 100
total_labels = df['Label'].nunique()
total_univers = df['Univers'].nunique()


st.write(f'**Nombre de produits au total :** {total_products}')
st.write(f'**% de produits avec le même libellé :** {duplicated_titles}')
st.write(f'**% de produits catégorisés :** {labelled_products}')
st.write(f'**Nombre de catégories :** {total_labels}')
st.write(f"**Nombre d'univers :** {total_univers}")

st.header('Cartographie de catégories de produits')
#Visualise sizes of supermarket categories (manually added to result_labelled) and clean clusters
df_summary = pd.pivot_table(df,index=['Label', 'Univers'],values=['Title'],aggfunc='count').reset_index().rename(columns={'Title':'count'})
df_treemap = df_summary[(df_summary['Label'] != '') & (df_summary['count'] > 1)]
fig = px.treemap(df_treemap,path=['Univers', 'Label'],values='count', width=1600, height=1000)
#fig.show();
st.plotly_chart(fig)

st.header('Echantillon de produits catégorisés')
st.table(df[:30])

