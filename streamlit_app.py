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
        # Carregar top 100 criptos
        @st.cache_data(ttl=3600)
        def load_top_cryptos():
            try:
 url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
                response = requests.get(url)
                data = response.json()
                return [(coin["id"], f"{coin['name']} ({coin['symbol'].upper()}) -${coin['current_price']:.2f}") for coin in data]
            except:
                return [("bitcoin", "Bitcoin (BTC)"), ("ethereum", "Ethereum (ETH)")]
        crypto_options = load_top_cryptos()
        selected_crypto = st.selectbox("🔍 Selecione a criptomoeda:", crypto_options,format_func=lambda x: x[1])
        col1, col2 = st.columns(2)
        with col1:
            quantidade = st.number_input("💎 Quantidade:", min_value=0.0, format="%.8f")
        with col2:
            preco_compra = st.number_input("💵 Preço de compra (USD):", min_value=0.0,format="%.2f")
        if st.button("✅ Adicionar ao Portfólio", type="primary"):
            if quantidade > 0 and preco_compra > 0:
                st.success(f"Adicionado: {quantidade} {selected_crypto[1]}")
            else:
                st.error("Preencha quantidade e preço!")
