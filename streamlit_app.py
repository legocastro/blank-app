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
      crypto_search = st.text_input("Buscar crypto:", placeholder="Ex: Bitcoin, BTC...")
      quantidade = st.number_input("Quantidade:", min_value=0.0)
      if crypto_search:
          try:
              url = f"https://api.coingecko.com/api/v3/search?query={crypto_search}"
              response = requests.get(url)
              results = response.json()["coins"][:5]  
              if results:
                  crypto_options = [(coin["id"], f"{coin['name']} ({coin['symbol'].upper()})") for coin in results]
                  selected = st.selectbox("Selecione a criptomoeda:", crypto_options, format_func=lambda x: x[1])
                  crypto_id = selected[0]
                  st.success(f"Selecionado: {selected[1]}")
              else:  
                  st.warning("Nenhuma criptomoeda encontrada")
          except: 
              st.error("Erro na busca. Tente novamente.")
            
