import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Mapa de Identidad", page_icon="🎯", layout="centered")

st.title("🎯 El Círculo de Mi Voz")
st.write("Escribe los elementos de cada capa y asígnales el peso que tienen en tu vida.")

# Función auxiliar para generar inputs dinámicos basados en lo que escribe el usuario
def generar_inputs(items, color_tema):
    valores = []
    if not items or items[0] == "":
        return []
    
    st.markdown(f"**{color_tema}**")
    for item in items:
        # Se calcula un valor equitativo por defecto (ej: si son 4, arranca en 25%)
        valor_defecto = max(1, 100 // len(items))
        val = st.number_input(f"{item} (%)", min_value=1, max_value=100, value=valor_defecto, key=f"num_{color_tema}_{item}")
        valores.append(val)
    return valores

# --- PASO 1: INGRESAR ELEMENTOS ---
with st.expander("📝 1. Ingresa tus elementos (separados por coma)", expanded=True):
    entorno_txt = st.text_input("🌍 Tu Entorno", "Resistencia, UTN, Gym")
    roles_txt = st.text_input("🤝 Tus Roles", "Hija, deportista, madre perruna")
    nucleo_txt = st.text_input("✨ Tu Núcleo", "Lealtad, justicia, creatividad")

# Limpiamos los textos y los convertimos en listas
entorno_items = [x.strip() for x in entorno_txt.split(",") if x.strip()]
roles_items = [x.strip() for x in roles_txt.split(",") if x.strip()]
nucleo_items = [x.strip() for x in nucleo_txt.split(",") if x.strip()]

# --- PASO 2: ASIGNAR PORCENTAJES ---
with st.expander("⚖️ 2. Asigna el porcentaje a cada elemento", expanded=True):
    st.write("Indica qué tanto peso tiene cada parte en esa capa. (El gráfico ajustará las porciones automáticamente).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        entorno_vals = generar_inputs(entorno_items, "🌍 Entorno")
    with col2:
        roles_vals = generar_inputs(roles_items, "🤝 Roles")
    with col3:
        nucleo_vals = generar_inputs(nucleo_items, "✨ Núcleo")

# --- PASO 3: GRAFICAR ---
if st.button("🚀 Generar Mi Gráfico Interactivo", use_container_width=True):
    st.divider()
    
    fig = go.Figure()

    # Capa Exterior (Entorno) - Anillo más grande
    fig.add_trace(go.Pie(
        labels=entorno_items, values=entorno_vals,
        domain=dict(x=[0.0, 1.0], y=[0.0, 1.0]),
        hole=0.7, sort=False, direction='clockwise',
        textinfo='label+percent', textposition='inside',
        marker=dict(colors=['#90CAF9', '#64B5F6', '#42A5F5', '#2196F3', '#1976D2']),
        insidetextorientation='radial'
    ))

    # Capa Intermedia (Roles) - Anillo del medio
    fig.add_trace(go.Pie(
        labels=roles_items, values=roles_vals,
        domain=dict(x=[0.15, 0.85], y=[0.15, 0.85]),
        hole=0.5, sort=False, direction='clockwise',
        textinfo='label+percent', textposition='inside',
        marker=dict(colors=['#FFCC80', '#FFB74D', '#FFA726', '#FF9800', '#F57C00']),
        insidetextorientation='radial'
    ))

    # Capa Interna (Núcleo) - Círculo central
    fig.add_trace(go.Pie(
        labels=nucleo_items, values=nucleo_vals,
        domain=dict(x=[0.325, 0.675], y=[0.325, 0.675]),
        hole=0.0, sort=False, direction='clockwise',
        textinfo='label+percent', textposition='inside',
        marker=dict(colors=['#F48FB1', '#F06292', '#E91E63', '#C2185B', '#880E4F']),
        insidetextorientation='horizontal'
    ))

    # Diseño final sin bordes y centrado
    fig.update_layout(
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=False,
        height=650
    )

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Tip interactivo:** ¡Tú o tu mentoreada pueden tocar o pasar el mouse sobre cada porción del gráfico para ver los valores exactos resaltados!")
