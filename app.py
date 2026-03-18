
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(page_title="Pavimentação Intelligence", layout="wide")

st.title("📊 Dashboard de Orçamentação de Pavimentação")
st.caption("Engenharia de Custos baseada em Dados (Física + Data Science)")

# --- SIDEBAR: INPUTS ---
with st.sidebar:
    st.header("⚙️ Parâmetros da Obra")
    area = st.number_input("Área Total (m²)", min_value=1.0, value=5000.0)
    espessura = st.number_input("Espessura (cm)", min_value=1.0, value=5.0)
    bdi = st.slider("BDI (%)", 0, 40, 25)
    
    st.divider()
    st.subheader("➕ Adicionar Insumo")
    nome_insumo = st.text_input("Material/Serviço")
    tipo = st.selectbox("Cálculo", ["Tonelagem (CBUQ)", "Área (m²)", "Verba/Global"])
    preco_un = st.number_input("Preço Unitário (R$)", min_value=0.0)
    
    if st.button("Adicionar ao Orçamento"):
        if 'dados' not in st.session_state:
            st.session_state.dados = []
        
        if "Tonelagem" in tipo:
            qtd = (area * (espessura / 100)) * 2.4
        elif "Área" in tipo:
            qtd = area
        else:
            qtd = 1.0
            
        st.session_state.dados.append({
            "Item": nome_insumo, "Qtd": qtd, "Un": "Ton" if "Ton" in tipo else ("m²" if "Área" in tipo else "VB"), 
            "Unitário": preco_un, "Subtotal": qtd * preco_un
        })

# --- CORPO PRINCIPAL ---
if 'dados' in st.session_state and len(st.session_state.dados) > 0:
    df = pd.DataFrame(st.session_state.dados)
    custo_direto = df['Subtotal'].sum()
    total_obra = custo_direto * (1 + bdi/100)

    col1, col2, col3 = st.columns(3)
    col1.metric("Custo Direto", f"R$ {custo_direto:,.2f}")
    col2.metric("Total com BDI", f"R$ {total_obra:,.2f}")
    col3.metric("Preço por m²", f"R$ {(total_obra/area):,.2f}")

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        fig_pizza = px.pie(df, values='Subtotal', names='Item', title="Distribuição de Custos", hole=0.4)
        st.plotly_chart(fig_pizza, use_container_width=True)
    with c2:
        st.subheader("📋 Detalhamento")
        st.dataframe(df, use_container_width=True)

    if st.button("🗑️ Reiniciar"):
        st.session_state.dados = []
        st.rerun()
else:
    st.info("Adicione itens na barra lateral para começar.")
