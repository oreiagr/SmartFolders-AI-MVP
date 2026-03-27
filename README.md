# SmartFolders AI 🪄📂

SmartFolders AI é um agente de Inteligência Artificial integrado nativamente ao menu de contexto do Windows Explorer. Ele permite processar arquivos locais utilizando LLMs diretamente pelo clique do botão direito, automatizando a criação de pastas e organização de dados extraídos.

## 🚀 O Projeto (MVP)

A proposta principal é transformar o sistema de arquivos do sistema operacional em um pipeline visual de dados. Em vez de abrir o navegador ou um software de terceiros, o processamento ocorre onde o arquivo já reside.

Nesta primeira versão (MVP), o script manipula o Registro do Windows para adicionar a opção **"🪄 Resumir com SmartFolder AI"** em arquivos de texto (`.txt`), consumindo a API do Google Gemini para processar o conteúdo e gerar diretórios filhos organizados dinamicamente com as respostas.

## ⚙️ Tecnologias Utilizadas
- **Python 3.x**
- **Google GenAI API** (Modelo Gemini 2.5 Flash)
- **Windows Registry API** (`winreg`)
- **OS & Sys libraries** para manipulação de rotas de sistema

## 🔧 Instalação e Configuração

1. Clone o repositório:
```bash
git clone [https://github.com/SEU_USUARIO/SmartFolders-AI-MVP.git](https://github.com/SEU_USUARIO/SmartFolders-AI-MVP.git)

2 Instale a dependência da API:
pip install google-genai


3 Configure sua API Key:
No arquivo smart_folder.py, insira sua chave obtida no Google AI Studio:
GOOGLE_API_KEY = "SUA_CHAVE_DE_API_AQUI"

4 Adicione ao Menu de Contexto do Windows:
Abra o terminal como Administrador e execute o setup:
python setup.py

🗺️ Roadmap e Próximos Passos
O projeto escalará para uma arquitetura de múltiplos níveis (Pipeline Visual):

[x] MVP: Integração via Registro do Windows e consumo de API.

[ ] Interface Dinâmica (GUI) com Tkinter/CustomTkinter para seleção de prompts personalizados.

[ ] Nível 2 (Processamento de Dados): OCR em imagens e PDFs.

[ ] Nível 3 (Análise de Negócios): Geração estruturada para consumo em BI (JSON/CSV).

Desenvolvido por Donavan Chagas | Estudante de Inteligência Artificial da PUCPR
