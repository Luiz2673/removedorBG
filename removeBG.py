import streamlit as st
from rembg import remove
from PIL import Image
import io
import os

st.set_page_config(page_title="🎯 Removedor de Fundo", layout='centered')
st.markdown("<h1 style='text-align: center; color: white;'>🖼️ Removedor de Fundo Automático</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Envie uma imagem e remova o fundo em segundos!</p>", unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    st.header("⚙️ Configurações")
    upload_file = st.file_uploader("📂 Escolha uma imagem:")
    processar = st.button("🚀 Processar imagem")

if processar:
    if upload_file is not None:
        ext = os.path.splitext(upload_file.name)[1].lower() #Verifica o tipo de arquivo e coloca em lower após o.
        if ext not in ['.jpg', '.jpeg', '.png']:
            st.error("❌ Tipo de arquivo inválido. Envie uma imagem .jpg, .jpeg ou .png.")
        else:
            with st.spinner("Processando imagem..."):
                try:
                    inp = Image.open(upload_file)
                    output = remove(inp)

                    st.markdown("### 🖼️ Imagem Original")
                    st.image(inp, use_container_width=True)

                    st.markdown("### 🧼 Imagem Sem Fundo")
                    st.image(output, use_container_width=True)

                    buf = io.BytesIO()
                    output.save(buf, format="PNG")
                    byte_im = buf.getvalue()

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
