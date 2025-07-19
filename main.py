import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
import pathlib

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Define o caminho base do script para encontrar arquivos de forma segura
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

def init():
    """
    Inicializa a aplicação, carregando variáveis de ambiente e configurando a página.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Verifica se a chave da API da OpenAI está presente e exibe um erro na interface se não estiver
    if not os.getenv("OPENAI_API_KEY"):
        st.error("🔑 Chave da API da OpenAI não encontrada! Por favor, configure seu arquivo .env.")
        st.stop()  # Interrompe a execução da aplicação de forma elegante

    # Configurações da página do Streamlit
    st.set_page_config(
        page_title="Chat Inteligente",
        page_icon="🤖"
    )

    # Carrega e exibe o vídeo de forma segura
    video_path = SCRIPT_DIR / "video" / "cipaa_exclusivo.mp4"
    try:
        with open(video_path, 'rb') as video_file:
            video_bytes = video_file.read()
        st.video(video_bytes)
    except FileNotFoundError:
        st.warning("Arquivo de vídeo 'cipaa_exclusivo.mp4' não encontrado na pasta 'video'.")

def main():
    """
    Função principal que executa a lógica do chatbot.
    """
    init()
    
    chat = ChatOpenAI(temperature=0)
    
    # Inicializa o histórico de mensagens no estado da sessão se não existir
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Você é um assistente virtual especialista em Segurança do Trabalho e Meio Ambiente."),
        ]
    
    st.header("NOSSO CHAT AQUI DA DESA")
    st.subheader("Saiba mais sobre Segurança e Meio Ambiente", divider="rainbow")
    
    # Campo de entrada do usuário
    user_input = st.text_input("Pergunte algo sobre segurança ou meio ambiente:", key="user_input")
    
    if user_input:
        # Adiciona a mensagem do usuário ao histórico
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Exibe um spinner enquanto a resposta da IA está sendo gerada
        with st.spinner("Analisando sua pergunta..."):
            response = chat(st.session_state.messages)
        
        # Adiciona a resposta da IA ao histórico
        st.session_state.messages.append(AIMessage(content=response.content))
        
    # Exibe o histórico de mensagens de forma robusta
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):  # Pula a SystemMessage inicial que não é para ser exibida
        # Verifica o tipo da mensagem para definir quem é o autor
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=f"{i}_user")
        elif isinstance(msg, AIMessage):
            message(msg.content, is_user=False, key=f"{i}_ai")

if __name__ == "__main__":
    main()
