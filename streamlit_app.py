import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json
st.set_page_config(page_title="My Crypto Portfolio", layout="wide")
st.title("My Crypto Portfolio")
tab1, tab2 = st.tabs(["Dashboard", "Adicionar Ativo"])
with tab1:
      st.header("Meu Dashboard")
      st.success("Funcionando!")
with tab2:
      st.header("Adicionar Ativo")
      crypto = st.text_input("Buscar crypto:")
      quantidade = st.number_input("Quantidade:", min_value=0.0)
      if st.button("Adicionar"):
            st.success("Adicionado!")
