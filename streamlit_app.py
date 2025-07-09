import streamlit as st
  import requests
  import pandas as pd
  from datetime import datetime
  import json

  st.set_page_config(
      page_title="💰 My Crypto Portfolio",
      page_icon="💰",
      layout="wide"
  )

  st.title("💰 My Crypto Portfolio")

  tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "➕ Adicionar Ativo", "⚙️ Configurações"])

  with tab1:
      st.header("📊 Meu Dashboard")
      st.success("Portfólio funcionando perfeitamente online!")

      col1, col2, col3, col4 = st.columns(4)
      with col1:
          st.metric("💰 Valor Total", "$0.00")
      with col2:
          st.metric("📈 P&L Total", "$0.00", "0%")
      with col3:
          st.metric("🪙 Ativos" , "0")
      with col4:
          st.metric("🕐 Status", "Online", "✅")

  with tab2:
      st.header("➕ Adicionar Novo Ativo")

      search_crypto = st.text_input("🔍 Buscar criptomoeda:", placeholder="Ex: Bitcoin, BTC...")

      col1, col2 = st.columns(2)
      with col1:
          quantidade = st.number_input("💎 Quantidade:", min_value=0.0, format="%.8f")
      with col2:
          preco = st.number_input("💵 Preço de compra (USD):", min_value=0.0, format="%.2f")

      if st.button("✅ Adicionar ao Portfólio", type="primary"):
          st.success("Ativo será adicionado!")

  with tab3:
      st.header("⚙️ Configurações")
      st.write("Configurações do portfólio")

  st.markdown("---")
  st.markdown("📊 *Powered by CoinGecko API*")
