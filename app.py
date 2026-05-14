import streamlit as st

# Configuración de página
st.set_page_config(page_title="Mapa de Identidad", page_icon="🎯")

# Título
st.title("🎯 El Círculo de Mi Voz")
st.write("Completa tus capas para generar tu gráfico circular.")

# Entradas de datos (usando text_input para que el texto no sea excesivamente largo)
with st.container():
    entorno = st.text_input("🌍 Tu Entorno", "Resistencia, UTN, Gym")
    roles = st.text_input("🤝 Tus Roles", "Hija, deportista, madre perruna")
    valores = st.text_input("✨ Tu Núcleo", "Lealtad, creatividad, pasear con Mocca")

# Botón de generar
if st.button("🚀 Generar Mi Círculo", use_container_width=True):
    st.divider()
    
    # HTML sin sangrías para armar círculos perfectos
    circulos_html = f"""
<div style="display: flex; justify-content: center; padding: 20px; font-family: sans-serif;">
<div style="width: 380px; height: 380px; border-radius: 50%; background-color: #E3F2FD; border: 3px solid #2196F3; display: flex; align-items: center; justify-content: center; position: relative; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
<div style="position: absolute; top: 25px; width: 250px; color: #0D47A1;">
<b style="font-size: 1.1em;">🌍 ENTORNO</b><br>
<span style="font-size: 0.9em;">{entorno}</span>
</div>
<div style="width: 260px; height: 260px; border-radius: 50%; background-color: #FFF3E0; border: 3px solid #FF9800; display: flex; align-items: center; justify-content: center; position: relative; z-index: 2; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
<div style="position: absolute; top: 20px; width: 180px; color: #E65100;">
<b style="font-size: 1.1em;">🤝 ROLES</b><br>
<span style="font-size: 0.9em;">{roles}</span>
</div>
<div style="width: 140px; height: 140px; border-radius: 50%; background-color: #FCE4EC; border: 3px solid #F06292; display: flex; align-items: center; justify-content: center; z-index: 3; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
<div style="color: #880E4F;">
<b style="font-size: 1.1em;">✨ NÚCLEO</b><br>
<span style="font-size: 0.85em;">{valores}</span>
</div>
</div>
</div>
</div>
</div>
"""
    st.markdown(circulos_html, unsafe_allow_html=True)
    
    st.success("¡Círculo generado con éxito!")
    st.info("💡 **Reflexión:** De todas estas capas que acabas de armar, si hoy tuvieras que usar un megáfono... ¿Desde qué parte de este círculo te gustaría hablarle al mundo?")
