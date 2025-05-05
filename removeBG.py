import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="🎯 Removedor de Fundo", layout='centered')
st.markdown("<h1 style='text-align: center; color: white;'>🖼️ Removedor de Fundo Automático</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Envie uma imagem e remova o fundo em segundos!</p>", unsafe_allow_html=True)

# Barra lateral
with st.sidebar:
    st.header("⚙️ Configurações")
    upload_file = st.file_uploader("📂 Escolha uma imagem:", type=['jpg', 'jpeg', 'png'])
    processar = st.button("🚀 Processar imagem")

if processar:
    if upload_file is not None:
        with st.spinner("Processando imagem..."):
            try:
                # Abrir imagem original
                inp = Image.open(upload_file)
                output = remove(inp)

                # Mostrar imagens centralizadas
                st.markdown("### 🖼️ Imagem Original")
                st.image(inp, use_container_width=True)

                st.markdown("### 🧼 Imagem Sem Fundo")
                st.image(output, use_container_width=True)

                # Preparar imagem para download
                buf = io.BytesIO()
                output.save(buf, format="PNG")
                byte_im = buf.getvalue()

                # Botão de download
                st.download_button(
                    label="⬇️ Baixar imagem sem fundo",
                    data=byte_im,
                    file_name="sem_fundo.png",
                    mime="image/png"
                )

            except Exception as e:
                st.error(f"Erro ao processar a imagem: {e}")
    else:
        st.warning("⚠️ Por favor, envie uma imagem antes de processar.")
