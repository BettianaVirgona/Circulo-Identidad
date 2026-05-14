import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Círculo de Identidad | Mi Voz",
    page_icon="🎯",
    layout="centered"
)

# Estilos CSS personalizados para simular las capas concéntricas en los resultados
st.markdown("""
    <style>
    .capa-exterior {
        background-color: #e8f4f8; 
        padding: 30px; 
        border-radius: 20px; 
        border: 2px solid #b3d9e6;
        text-align: center;
    }
    .capa-intermedia {
        background-color: #fff3e6; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #ffcc99;
        margin-top: 15px;
    }
    .capa-nucleo {
        background-color: #fce4ec; 
        padding: 30px; 
        border-radius: 10px; 
        border: 2px solid #f48fb1;
        margin-top: 15px;
    }
    .titulo-capa {
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Título y bienvenida
st.title("🎯 El Mapa de Mi Voz")
st.markdown("""
¡Bienvenida! Tu identidad es como una gran caja de resonancia. 
Vamos a construir juntas tu **Círculo de Identidad** para descubrir desde dónde puedes hacer escuchar tu voz.
""")

st.divider()

# Formularios de entrada divididos en pestañas o expansores
st.subheader("Paso 1: Construyendo las capas")

with st.expander("✨ Capa 1: Mi Núcleo (El 'Yo' íntimo)", expanded=True):
    st.write("Aquí van tus valores más profundos y lo que te hace única.")
    valores = st.text_area("¿Cuáles son los 3 valores que no negocias? (Ej: Lealtad, creatividad, justicia)", height=68)
    pasiones = st.text_area("¿Qué cosas te apasionan hacer o aprender?", height=68)

with st.expander("🤝 Capa 2: Mis Roles (Los Vínculos)", expanded=False):
    st.write("Los lugares que ocupas cuando te relacionas con otras personas.")
    roles = st.text_input("¿Qué roles ocupas en tu vida diaria? (Ej: Hija, amiga, estudiante, deportista, etc.)")

with st.expander("🌍 Capa 3: Mi Entorno (El Mundo Exterior)", expanded=False):
    st.write("Tus influencias y cómo interactúas con la sociedad.")
    grupos = st.text_input("¿De qué lugares, culturas o grupos sientes que formas parte?")
    etiquetas = st.text_input("¿Qué 'etiquetas' sientes que a veces te pone el resto de la gente?")

st.divider()

# Botón para generar el mapa
if st.button("Generar Mi Mapa de Identidad 🚀", use_container_width=True):
    if valores and roles and grupos: # Validación rápida
        st.subheader("Tu Círculo de Identidad Terminado")
        st.markdown("Así se compone tu identidad desde el exterior hacia tu núcleo más profundo:")
        
        # Renderizado visual de las capas (usando el CSS definido arriba)
        st.markdown(f"""
        <div class="capa-exterior">
            <div class="titulo-capa">🌍 Capa Exterior: El Entorno</div>
            <b>Grupos a los que pertenezco:</b> {grupos} <br>
            <b>Etiquetas del entorno:</b> {etiquetas}
            
            <div class="capa-intermedia">
                <div class="titulo-capa">🤝 Capa Intermedia: Mis Roles</div>
                {roles}
                
                <div class="capa-nucleo">
                    <div class="titulo-capa">✨ El Núcleo: Quién Soy</div>
                    <b>Mis Valores:</b> {valores} <br><br>
                    <b>Mis Pasiones:</b> {pasiones}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("¡Mapa generado con éxito!")
        
        # Pregunta de Coaching para el final
        st.info("💡 **Reflexión para charlar con tu mentora:** De todas estas capas que acabas de armar, si hoy tuvieras que usar un megáfono... ¿Desde qué parte de este círculo te gustaría hablarle al mundo?")
    else:
        st.warning("Por favor, completa al menos un campo en cada capa para poder generar tu mapa.")
