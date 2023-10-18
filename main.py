import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()
    if os.getenv('OPENAI_API_KEY') is None or os .getenv('OPENAI_API_KEY') == "":
        print("A chave da API do OpenAI não está configurada")
        exit(1)
    else:
        print("O OpenAI está configurado")
    
    
    st.set_page_config(
        page_title="Chat DESA",
        page_icon="🤖"
    )

    imagem = st.image('./img/segurencio.png')

def main():
    init()
    
    chat = ChatOpenAI(temperature=0)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Um assistente virtual"),
        ]
    
    st.header("NOSSO CHAT AQUI DA DESA")
    st.subheader("Saiba mais sobre Segurança e Meio Ambiente",divider="rainbow") 
    
    user_input = st.text_input("Pergunte algo", key="user_input")
    
    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Pensando..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')
            
    
if __name__ == "__main__":
    main()