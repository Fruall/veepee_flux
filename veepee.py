import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px

st.header("Veepee Flux")


df = pd.read_csv('veepee_catalog_final.csv', sep=';', encoding='utf-8')
#df = pd.read_excel('veepee_catalog_final.xlsx')

#df = pd.read_excel('veepee_catalog_final.xlsx', engine='openpyxl')

df = df[['Title', 'Label', 'Univers']]
#st.table(df[:30])

#Visualise sizes of supermarket categories (manually added to result_labelled) and clean clusters
df_summary = pd.pivot_table(df,index=['Label', 'Univers'],values=['Title'],aggfunc='count').reset_index().rename(columns={'Title':'count'})
df_treemap = df_summary[(df_summary['Label'] != '') & (df_summary['count'] > 1)]
fig = px.treemap(df_treemap,path=['Univers', 'Label'],values='count')
fig.show();
