### Bem Vindo ao Removedor de Background Streamlit

## 🚀 Funcionalidades

*   **Interface Web Intuitiva:** Fácil de usar, criada com a biblioteca Streamlit.
*   **Upload Flexível:** Suporta upload de imagens nos formatos `JPG`, `JPEG` e `PNG`.
*   **Remoção Automática:** Utiliza a poderosa biblioteca `rembg` para identificar e remover o fundo da imagem.
*   **Visualização Instantânea:** Compare a imagem original com a imagem processada lado a lado.
*   **Download Fácil:** Baixe a imagem resultante (sem fundo) em formato `PNG` com apenas um clique.

## 🛠️ Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Streamlit:** Framework para criação rápida de aplicativos web para data science e ML.
*   **rembg:** Biblioteca para remoção de fundo de imagens.
*   **Pillow (PIL):** Biblioteca para manipulação de imagens em Python.

## ⚙️ Instalação e Execução Local

Siga os passos abaixo para executar o aplicativo na sua máquina local:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Luiz2673/removedorBG.git 
    cd removedorBG 
    ```

2.  **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**
    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install streamlit rembg Pillow
    ```
    *(Se você criar um arquivo `requirements.txt`, pode usar `pip install -r requirements.txt`)*

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run removeBG.py 
    ```
5.  O aplicativo abrirá automaticamente no seu navegador padrão.

## 💡 Como Usar

1.  Execute o aplicativo conforme as instruções de instalação.
2.  Na barra lateral ("⚙️ Configurações"), clique em "📂 Escolha uma imagem:" para fazer o upload do seu arquivo (`.jpg`, `.jpeg` ou `.png`).
3.  Após selecionar a imagem, clique no botão "🚀 Processar imagem".
4.  Aguarde alguns segundos enquanto a imagem é processada (você verá a mensagem "Processando imagem...").
5.  A imagem original e a imagem com o fundo removido serão exibidas na área principal.
6.  Clique no botão "⬇️ Baixar imagem sem fundo" para salvar o resultado no seu computador como `sem_fundo.png`.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para:

1.  Fazer um Fork do projeto.
2.  Criar uma Branch para sua feature (`git checkout -b feature/NovaFuncionalidade`).
3.  Fazer Commit de suas mudanças (`git commit -m 'Adiciona NovaFuncionalidade'`).
4.  Fazer Push para a Branch (`git push origin feature/NovaFuncionalidade`).
5.  Abrir um Pull Request.

Você também pode abrir uma *Issue* para reportar problemas ou sugerir ideias.