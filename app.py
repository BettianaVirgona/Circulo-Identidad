import streamlit as st

# Configuración de página
st.set_page_config(page_title="Mapa de Identidad", page_icon="🎯")

# Título
st.title("🎯 El Mapa de Mi Voz")
st.write("Completa las capas de tu identidad para generar tu mapa visual.")

# Estilos CSS (Directo y simple)
st.markdown("""
<style>
    .box { border-radius: 15px; padding: 20px; margin: 10px 0px; border: 2px solid; }
    .exterior { background-color: #E3F2FD; border-color: #2196F3; color: #0D47A1; }
    .intermedia { background-color: #FFF3E0; border-color: #FF9800; color: #E65100; margin-left: 20px; }
    .nucleo { background-color: #FCE4EC; border-color: #F06292; color: #880E4F; margin-left: 40px; }
    .label { font-weight: bold; text-transform: uppercase; font-size: 0.8em; display: block; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# Entradas de datos
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        entorno = st.text_input("🌍 Tu Entorno (Grupos, ciudad, etiquetas)", "Resistencia, UTN, Gym")
    with col2:
        roles = st.text_input("🤝 Tus Roles (Hija, estudiante, etc.)", "Hija, deportista")
    
    valores = st.text_area("✨ Tu Núcleo (Valores y Pasiones)", "Lealtad, creatividad...")

# Botón de generar
if st.button("🚀 Generar Mi Mapa Visual", use_container_width=True):
    st.divider()
    
    # Capa Exterior
    st.markdown(f"""
    <div class="box exterior">
        <span class="label">🌍 Capa Exterior: El Entorno</span>
        {entorno}
        
        <div class="box intermedia">
            <span class="label">🤝 Capa Intermedia: Mis Roles</span>
            {roles}
            
            <div class="box nucleo">
                <span class="label">✨ El Núcleo: Quién Soy</span>
                {valores}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("¡Mapa generado con éxito!")
    st.info("💡 **Pregunta para tu mentora:** ¿Desde qué parte de este círculo te gustaría hablarle al mundo hoy?")
