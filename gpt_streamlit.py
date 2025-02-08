import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def check_login():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    
    if not st.session_state["authenticated"]:
        with st.form("login_form"):
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                if username == "admin" and password == "admin":
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.warning("Usuário ou senha incorretos.")
                    return False
        return False
    return True

def logout():
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

def main():
    st.set_page_config(page_title="Dashboard Vena", layout="wide")
    
    if not check_login():
        return
    
    logout()
    
    # Header
    st.markdown("""
        <div style='background-color: #5A9BF6; padding: 10px; text-align: left;'>
            <h1 style='color: white;'>Vena.</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados de exemplo
    data = {
        "Categoria": ["P1 - Gestão Comercial", "P2 - Experiência Omni & Digital", "P3 - ESG", "P4 - Excelência Operacional", "P5 - Gestão de Pessoas e Finanças"],
        "Atual": [425, 222, 70, 120, 45],
        "Meta": [470, 240, 85, 120, 45]
    }
    df = pd.DataFrame(data)
    
    # Gauge Chart (Indicador de classificação)
    st.subheader("Classificação Parcial")
    st.markdown("""
        <div style='text-align: center;'>
            <h2>93,42%</h2>
            <p>Ouro</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Gráfico de Barras
    st.subheader("Pontuação por Categoria")
    fig_bar = px.bar(df, x="Categoria", y=["Atual", "Meta"], barmode="group", 
                     labels={"value": "Pontuação", "variable": "Legenda"}, 
                     title="Comparação de Pontuação")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Gráfico Radar
    st.subheader("Meta vs. Atingido")
    fig_radar = px.line_polar(df, r="Atual", theta="Categoria", line_close=True,
                              title="Radar Chart - Desempenho")
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Posição de Pontos a Conquistar
    pontos_conquistar = {
        "Categoria": ["P1", "P2", "P3", "P4", "P5"],
        "Pontos": [45, 18, 15, 0, 0]
    }
    df_pontos = pd.DataFrame(pontos_conquistar)
    
    st.subheader("Pontos a Conquistar")
    fig_pontos = px.bar(df_pontos, x="Categoria", y="Pontos", title="Pontos Restantes por Categoria")
    st.plotly_chart(fig_pontos, use_container_width=True)
    
    # Half Pie Chart com mais de um item
    st.subheader("Distribuição de Categorias")
    fig_half_pie = go.Figure()
    fig_half_pie.add_trace(go.Pie(labels=df["Categoria"], values=df["Atual"], hole=0.6, direction='clockwise',
                                   domain={'x': [0, 1], 'y': [0, 0.5]}))
    fig_half_pie.update_layout(title_text="Distribuição de Pontuação por Categoria", showlegend=True)
    st.plotly_chart(fig_half_pie, use_container_width=True)
    
    st.write("A atualização dos dados pode diferir do consolidado acima. Atualização: 12/08/2024")
    
if __name__ == "__main__":
    main()
