import streamlit as st
import pandas as pd
import plotly.express as px

# Função para verificar o login
def check_login(username, password):
    # Aqui você pode implementar uma lógica de verificação de login mais segura
    return username == "admin" and password == "password"

# Página de Login
def login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Login"):
        if check_login(username, password):
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos")

# Página Principal com Gráfico
def main_page():
    st.title("AvVena")
    st.header("Ouro")
    st.write("Classificação Parcial: 93,42%")
    st.write("10 de ago 2024  868/960")

    # Dados para o gráfico
    categorias = ["P1 - Gestão Comercial", "P2 - Experiência Omni & Digital", "P3 - ESG", "P4 - Excelência Operacional", "P5 - Gestão de Pessoas e Finanças"]
    valores = [93.42, 85.0, 78.0, 88.0, 90.0]

    # Criando um DataFrame
    df = pd.DataFrame({
        "Categoria": categorias,
        "Valores": valores
    })

    # Criando o gráfico de barras com Plotly
    fig = px.bar(df, x="Categoria", y="Valores", text="Valores",
                 title="Classificação por Categoria",
                 labels={"Valores": "Valor (%)", "Categoria": "Categoria"},
                 color="Categoria",
                 color_discrete_sequence=px.colors.qualitative.Pastel)

    # Personalizando o layout do gráfico
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(
        xaxis_title="Categoria",
        yaxis_title="Valor (%)",
        showlegend=False,
        template="plotly_white",
        yaxis=dict(range=[0, 100]),  # Definindo o limite do eixo Y
    )

    # Exibindo o gráfico
    st.plotly_chart(fig)

    st.write("---")
    st.write("A atualização dos dados abaixo pode diferir do consolidado acima. Atualização: 12/08/2024")

# Configuração da Sessão
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Renderização da Página
if st.session_state['logged_in']:
    main_page()
else:
    login_page()