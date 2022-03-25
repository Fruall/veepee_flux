import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
from tqdm import tqdm, tqdm_notebook
import xlrd

st.header("Veepee Flux")


df = pd.read_csv('veepee_catalog_final.csv', sep=';', encoding='utf-8')
#df = pd.read_excel('veepee_catalog_final.xlsx')

#df = pd.read_excel('veepee_catalog_final.xlsx', engine='openpyxl')

df = df[['Title', 'Label', 'Univers']]
st.table(df[:30])

