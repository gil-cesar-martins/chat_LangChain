# 🤖 Chat com LangChain - Assistente Virtual de Segurança e Meio Ambiente

Um chatbot interativo e inteligente construído com Streamlit e LangChain, projetado para ser um assistente virtual especialista em tópicos de Segurança do Trabalho e Meio Ambiente. A aplicação utiliza o poder dos modelos de linguagem da OpenAI para fornecer respostas informativas e contextuais em tempo real.

---

## 🚀 Funcionalidades

* **Interface de Chat Intuitiva:** Interface limpa e amigável para uma conversa fluida.
* **Respostas por IA:** Utiliza a API da OpenAI através do LangChain para gerar respostas inteligentes.
* **Histórico de Conversa:** Mantém o contexto da conversa durante a sessão do usuário.
* **Foco Temático:** O `SystemMessage` inicial direciona o assistente para atuar como um especialista em Segurança e Meio Ambiente.
* **Feedback Visual:** Exibe uma animação de "Pensando..." enquanto a resposta está sendo processada.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

* **Python 3.10+**
* **Streamlit:** Para a criação da interface web interativa.
* **LangChain:** Framework para desenvolvimento de aplicações com modelos de linguagem.
* **OpenAI:** Para acesso ao modelo de linguagem GPT.
* **Streamlit-Chat:** Componente para criar a visualização de chat.
* **Python-Dotenv:** Para gerenciamento de variáveis de ambiente.

---

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

* [Python 3.10](https://www.python.org/) ou superior instalado.
* [Git](https://git-scm.com/) para clonar o repositório.
* Uma chave de API da [OpenAI](https://platform.openai.com/account/api-keys).

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Crie um arquivo `requirements.txt`** com as seguintes dependências:
    ```txt
    streamlit
    langchain
    openai
    streamlit-chat
    python-dotenv
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure suas credenciais:**
    * Renomeie o arquivo `.env.example` para `.env` (se você criar um) ou crie um novo arquivo chamado `.env`.
    * Adicione sua chave de API da OpenAI ao arquivo `.env`:
    ```
    OPENAI_API_KEY="sua-chave-de-api-aqui"
    ```

---

## ▶️ Como Executar

Com o ambiente virtual ativado e as dependências instaladas, inicie a aplicação com o seguinte comando:

```bash
streamlit run app.py
```

Abra seu navegador e acesse `http://localhost:8501`.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
> **Nota:** Certifique-se de adicionar um arquivo `LICENSE` ao seu repositório. Você pode escolher uma facilmente no próprio GitHub ao criar um novo arquivo. A licença MIT é uma ótima escolha para portfólios.
