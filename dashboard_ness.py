import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os

# Configuração da página
st.set_page_config(
    page_title="Dashboard Monstro do Lago Ness",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Arquivo para salvar os dados
DATA_FILE = "ness_data.json"

def load_data():
    """Carrega os dados do arquivo JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "materias": {
                "Análise de Dados": {"semana1": 0, "semana2": 0, "semana3": 0, "total": 0},
                "Fenômenos de Transporte": {"semana1": 0, "semana2": 0, "semana3": 0, "total": 0},
                "Circuitos Digitais": {"semana1": 0, "semana2": 0, "semana3": 0, "total": 0},
                "Desenvolvimento de Software": {"semana1": 0, "semana2": 0, "semana3": 0, "total": 0},
            },
            "historico": [],
            "ultima_atualizacao": datetime.now().isoformat()
        }

def save_data(data):
    """Salva os dados no arquivo JSON"""
    data["ultima_atualizacao"] = datetime.now().isoformat()
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_to_history(materia, semana, incremento):
    """Adiciona uma entrada ao histórico"""
    return {
        "timestamp": datetime.now().isoformat(),
        "materia": materia,
        "semana": semana,
        "incremento": incremento
    }

# Inicialização dos dados
if 'data' not in st.session_state:
    st.session_state.data = load_data()

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    .metric-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-card h4 {
        color: #333333;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    .metric-card p {
        color: #666666;
        margin: 0;
        font-size: 0.9rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
    .big-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🐉 Dashboard de Interações - Monstro do Lago Ness")
st.markdown("---")

# Sidebar para controles
with st.sidebar:
    st.header("🎮 Controles")
    
    # Seleção de matéria
    materias = list(st.session_state.data["materias"].keys())
    materia_selecionada = st.selectbox("Selecione a Matéria:", materias)
    
    # Seleção de semana
    semana_selecionada = st.selectbox("Selecione a Semana:", ["semana1", "semana2", "semana3"])
    semana_display = {"semana1": "Semana 1", "semana2": "Semana 2", "semana3": "Semana 3"}
    
    st.markdown("---")
    
    # Botões de incremento
    st.subheader(f"📚 {materia_selecionada}")
    st.write(f"🗓️ {semana_display[semana_selecionada]}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("➕ +1", key="plus1"):
            st.session_state.data["materias"][materia_selecionada][semana_selecionada] += 1
            st.session_state.data["materias"][materia_selecionada]["total"] += 1
            st.session_state.data["historico"].append(
                add_to_history(materia_selecionada, semana_selecionada, 1)
            )
            save_data(st.session_state.data)
            st.rerun()
    
    with col2:
        if st.button("➕ +5", key="plus5"):
            st.session_state.data["materias"][materia_selecionada][semana_selecionada] += 5
            st.session_state.data["materias"][materia_selecionada]["total"] += 5
            st.session_state.data["historico"].append(
                add_to_history(materia_selecionada, semana_selecionada, 5)
            )
            save_data(st.session_state.data)
            st.rerun()
    
    if st.button("➕ +10", key="plus10"):
        st.session_state.data["materias"][materia_selecionada][semana_selecionada] += 10
        st.session_state.data["materias"][materia_selecionada]["total"] += 10
        st.session_state.data["historico"].append(
            add_to_history(materia_selecionada, semana_selecionada, 10)
        )
        save_data(st.session_state.data)
        st.rerun()
    
    # Incremento personalizado
    st.markdown("---")
    incremento_custom = st.number_input("Incremento Personalizado:", min_value=1, max_value=100, value=1)
    if st.button(f"➕ +{incremento_custom}", key="custom"):
        st.session_state.data["materias"][materia_selecionada][semana_selecionada] += incremento_custom
        st.session_state.data["materias"][materia_selecionada]["total"] += incremento_custom
        st.session_state.data["historico"].append(
            add_to_history(materia_selecionada, semana_selecionada, incremento_custom)
        )
        save_data(st.session_state.data)
        st.rerun()
    
    st.markdown("---")

    # Seção de remoção de interações
    st.subheader("➖ Remover Interações")
    st.write(f"🗓️ {semana_display[semana_selecionada]}")

    colr1, colr2 = st.columns(2)
    with colr1:
        if st.button("➖ -1", key="minus1"):
            current = st.session_state.data["materias"][materia_selecionada][semana_selecionada]
            delta = min(1, current)
            if delta > 0:
                st.session_state.data["materias"][materia_selecionada][semana_selecionada] -= delta
                st.session_state.data["materias"][materia_selecionada]["total"] -= delta
                st.session_state.data["historico"].append(
                    add_to_history(materia_selecionada, semana_selecionada, -delta)
                )
                save_data(st.session_state.data)
                st.rerun()
    with colr2:
        if st.button("➖ -5", key="minus5"):
            current = st.session_state.data["materias"][materia_selecionada][semana_selecionada]
            delta = min(5, current)
            if delta > 0:
                st.session_state.data["materias"][materia_selecionada][semana_selecionada] -= delta
                st.session_state.data["materias"][materia_selecionada]["total"] -= delta
                st.session_state.data["historico"].append(
                    add_to_history(materia_selecionada, semana_selecionada, -delta)
                )
                save_data(st.session_state.data)
                st.rerun()

    if st.button("➖ -10", key="minus10"):
        current = st.session_state.data["materias"][materia_selecionada][semana_selecionada]
        delta = min(10, current)
        if delta > 0:
            st.session_state.data["materias"][materia_selecionada][semana_selecionada] -= delta
            st.session_state.data["materias"][materia_selecionada]["total"] -= delta
            st.session_state.data["historico"].append(
                add_to_history(materia_selecionada, semana_selecionada, -delta)
            )
            save_data(st.session_state.data)
            st.rerun()

    st.markdown("---")
    decremento_custom = st.number_input("Remoção Personalizada:", min_value=1, max_value=100, value=1, key="dec_custom_value")
    if st.button(f"➖ -{decremento_custom}", key="custom_remove"):
        current = st.session_state.data["materias"][materia_selecionada][semana_selecionada]
        delta = min(int(decremento_custom), current)
        if delta > 0:
            st.session_state.data["materias"][materia_selecionada][semana_selecionada] -= delta
            st.session_state.data["materias"][materia_selecionada]["total"] -= delta
            st.session_state.data["historico"].append(
                add_to_history(materia_selecionada, semana_selecionada, -delta)
            )
            save_data(st.session_state.data)
            st.rerun()

    st.markdown("---")
    if st.button("↩ Desfazer última interação", type="secondary", key="undo_last"):
        historico = st.session_state.data.get("historico", [])
        if historico:
            last = historico.pop()
            materia_last = last["materia"]
            semana_last = last["semana"]
            inc_last = last["incremento"]
            if inc_last > 0:
                # Reverter um incremento anterior
                available = st.session_state.data["materias"][materia_last][semana_last]
                delta = min(inc_last, available)
                if delta > 0:
                    st.session_state.data["materias"][materia_last][semana_last] -= delta
                    st.session_state.data["materias"][materia_last]["total"] -= delta
            elif inc_last < 0:
                # Reverter uma remoção anterior
                delta = abs(inc_last)
                st.session_state.data["materias"][materia_last][semana_last] += delta
                st.session_state.data["materias"][materia_last]["total"] += delta
            save_data(st.session_state.data)
            st.rerun()
        else:
            st.info("Não há interação para desfazer.")

    st.markdown("---")

    # Botão de reset
    if st.button("🔄 Reset Todos os Dados", type="secondary"):
        st.session_state.data = {
            "materias": {materia: {"semana1": 0, "semana2": 0, "semana3": 0, "total": 0} for materia in materias},
            "historico": [],
            "ultima_atualizacao": datetime.now().isoformat()
        }
        save_data(st.session_state.data)
        st.rerun()

# Layout principal
tab1, tab2, tab3, tab4 = st.tabs(["📊 Visão Geral", "📈 Gráficos", "📋 Tabela Detalhada", "📜 Histórico"])

with tab1:
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    total_geral = sum([dados["total"] for dados in st.session_state.data["materias"].values()])
    total_semana1 = sum([dados["semana1"] for dados in st.session_state.data["materias"].values()])
    total_semana2 = sum([dados["semana2"] for dados in st.session_state.data["materias"].values()])
    total_semana3 = sum([dados["semana3"] for dados in st.session_state.data["materias"].values()])
    
    with col1:
        st.metric("🎯 Total Geral", total_geral)
    with col2:
        st.metric("📅 Semana 1", total_semana1)
    with col3:
        st.metric("📅 Semana 2", total_semana2)
    with col4:
        st.metric("📅 Semana 3", total_semana3)
    
    st.markdown("---")
    
    # Cards por matéria
    st.subheader("📚 Interações por Matéria")
    
    for i, (materia, dados) in enumerate(st.session_state.data["materias"].items()):
        if i % 2 == 0:
            col1, col2 = st.columns(2)
        
        with col1 if i % 2 == 0 else col2:
            with st.container():
                st.markdown(f"""
                <div class="metric-card">
                    <h4>{materia}</h4>
                    <div class="big-number">{dados['total']}</div>
                    <p>S1: {dados['semana1']} | S2: {dados['semana2']} | S3: {dados['semana3']}</p>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.subheader("📈 Visualizações")
    
    # Preparar dados para gráficos
    df_materias = pd.DataFrame(st.session_state.data["materias"]).T
    df_materias.index.name = "Matéria"
    df_materias = df_materias.reset_index()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pizza - Total por matéria
        fig_pie = px.pie(
            df_materias, 
            values='total', 
            names='Matéria',
            title="🥧 Distribuição Total de Interações por Matéria",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Gráfico de barras - Total por matéria
        fig_bar = px.bar(
            df_materias, 
            x='Matéria', 
            y='total',
            title="📊 Total de Interações por Matéria",
            color='total',
            color_continuous_scale='Blues'
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Gráfico de barras empilhadas - Por semana
    df_semanas = df_materias.melt(
        id_vars=['Matéria'], 
        value_vars=['semana1', 'semana2', 'semana3'],
        var_name='Semana', 
        value_name='Interações'
    )
    df_semanas['Semana'] = df_semanas['Semana'].map({
        'semana1': 'Semana 1', 
        'semana2': 'Semana 2', 
        'semana3': 'Semana 3'
    })
    
    fig_stacked = px.bar(
        df_semanas, 
        x='Matéria', 
        y='Interações', 
        color='Semana',
        title="📈 Interações por Matéria e Semana",
        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
    )
    fig_stacked.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_stacked, use_container_width=True)

with tab3:
    st.subheader("📋 Tabela Detalhada")
    
    # Tabela formatada
    df_display = df_materias.copy()
    df_display.columns = ['Matéria', 'Semana 1', 'Semana 2', 'Semana 3', 'Total']
    
    # Adicionar linha de totais
    totals_row = {
        'Matéria': 'TOTAL',
        'Semana 1': df_display['Semana 1'].sum(),
        'Semana 2': df_display['Semana 2'].sum(),
        'Semana 3': df_display['Semana 3'].sum(),
        'Total': df_display['Total'].sum()
    }
    df_display = pd.concat([df_display, pd.DataFrame([totals_row])], ignore_index=True)
    
    # Destacar a linha de total
    def highlight_total(row):
        if row['Matéria'] == 'TOTAL':
            return ['background-color: #e6f3ff; font-weight: bold'] * len(row)
        return [''] * len(row)
    
    st.dataframe(
        df_display.style.apply(highlight_total, axis=1),
        use_container_width=True,
        hide_index=True
    )
    
    # Estatísticas adicionais
    st.markdown("---")
    st.subheader("📊 Estatísticas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        materia_mais_ativa = df_materias.loc[df_materias['total'].idxmax(), 'Matéria']
        st.metric("🏆 Matéria Mais Ativa", materia_mais_ativa, df_materias['total'].max())
    
    with col2:
        semana_mais_ativa = ['Semana 1', 'Semana 2', 'Semana 3'][
            [total_semana1, total_semana2, total_semana3].index(max([total_semana1, total_semana2, total_semana3]))
        ]
        st.metric("📅 Semana Mais Ativa", semana_mais_ativa, max([total_semana1, total_semana2, total_semana3]))
    
    with col3:
        media_por_materia = round(total_geral / len(materias), 1)
        st.metric("📈 Média por Matéria", f"{media_por_materia}")

with tab4:
    st.subheader("📜 Histórico de Interações")
    
    if st.session_state.data["historico"]:
        # Converter histórico em DataFrame
        df_historico = pd.DataFrame(st.session_state.data["historico"])
        df_historico['timestamp'] = pd.to_datetime(df_historico['timestamp'])
        df_historico = df_historico.sort_values('timestamp', ascending=False)
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            filtro_materia = st.selectbox("Filtrar por Matéria:", ["Todas"] + materias, key="filtro_hist")
        with col2:
            filtro_semana = st.selectbox("Filtrar por Semana:", ["Todas", "semana1", "semana2", "semana3"], key="filtro_sem_hist")
        
        # Aplicar filtros
        df_filtrado = df_historico.copy()
        if filtro_materia != "Todas":
            df_filtrado = df_filtrado[df_filtrado['materia'] == filtro_materia]
        if filtro_semana != "Todas":
            df_filtrado = df_filtrado[df_filtrado['semana'] == filtro_semana]
        
        # Mostrar histórico
        if not df_filtrado.empty:
            df_display_hist = df_filtrado.copy()
            df_display_hist['Data/Hora'] = df_display_hist['timestamp'].dt.strftime('%d/%m/%Y %H:%M:%S')
            df_display_hist = df_display_hist[['Data/Hora', 'materia', 'semana', 'incremento']]
            df_display_hist.columns = ['Data/Hora', 'Matéria', 'Semana', 'Incremento']
            df_display_hist['Semana'] = df_display_hist['Semana'].map({
                'semana1': 'Semana 1', 
                'semana2': 'Semana 2', 
                'semana3': 'Semana 3'
            })
            
            st.dataframe(df_display_hist, use_container_width=True, hide_index=True)
            
            # Gráfico de linha temporal
            st.subheader("📈 Evolução Temporal")
            df_historico['data'] = df_historico['timestamp'].dt.date
            df_timeline = df_historico.groupby('data')['incremento'].sum().reset_index()
            
            fig_timeline = px.line(
                df_timeline, 
                x='data', 
                y='incremento',
                title="Interações ao Longo do Tempo",
                markers=True
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
        else:
            st.info("Nenhuma interação encontrada com os filtros selecionados.")
    else:
        st.info("Ainda não há histórico de interações. Comece a usar os controles na barra lateral!")

# Rodapé
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.data.get("ultima_atualizacao"):
        ultima_att = datetime.fromisoformat(st.session_state.data["ultima_atualizacao"])
        st.caption(f"🕒 Última atualização: {ultima_att.strftime('%d/%m/%Y %H:%M:%S')}")

with col2:
    st.caption("🐉 Dashboard do Monstro do Lago Ness")

with col3:
    st.caption(f"💾 Total de registros: {len(st.session_state.data.get('historico', []))}")
