# Teste Bot WhatsApp

Bem-vindo ao projeto **Integração com API Bling**! Este repositório contém o código-fonte e a documentação para integração com API do Bling, desenvolvido usando Python e FastAPI. O objetivo é oferecer uma solução simples para dados da minha conta Bling ERP para minhas aplicações.

## ✨ Sumário

- [Links Úteis](#-links-%C3%BAteis)
- [TO-DO](#-to-do)
- [Comandos Git Flow](#comandos-git-flow)
- [Principais Recursos](#-principais-recursos)
- [Tecnologias Utilizadas](#%EF%B8%8F-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Configurar e Executar](#-como-configurar-e-executar)
- [Endpoints Disponíveis](#-endpoints-dispon%C3%ADveis)
- [Contribuições](#-contribui%C3%A7%C3%B5es)
- [Autor](#-autor)
- [Licença](#%F0%9F%8C%90-licen%C3%A7a)

## 🔗 Links Úteis

- [![Kanban do Projeto no Trello]()
- [![Configuração da API do Bling]()
- [![Padrões de Commits](https://img.shields.io/badge/Commits-Padr%C3%B5es-orange?logo=git)](https://github.com/iuricode/padroes-de-commits)

## 🔄 TO-DO
- [ ] Deploy automático no Digital Ocean
- [ ] Documentação da API automática
- [ ] Implementar logs para monitorar o desempenho e erros.
- [ ] Melhorar a documentação com exemplos práticos de uso.

## 🔀 Comandos Git Flow

Aqui estão os principais comandos para trabalhar com **Git Flow**:

### Inicializar Git Flow no Projeto
```bash
git flow init
```

### Criar uma Nova Feature
```bash
git flow feature start <nome-da-feature>
```

### Finalizar uma Feature
```bash
git flow feature finish <nome-da-feature>
```

### Criar uma Nova Release
```bash
git flow release start <versao-da-release>
```

### Finalizar uma Release
```bash
git flow release finish <versao-da-release>
```

### Criar um Hotfix
```bash
git flow hotfix start <nome-do-hotfix>
```

### Finalizar um Hotfix
```bash
git flow hotfix finish <nome-do-hotfix>
```

Esses comandos ajudam a organizar o desenvolvimento do projeto de forma estruturada, com ramificações para funcionalidades, correções e lançamentos.



## 💡 Principais Recursos
- 

## ⚙️ Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Framework**: FastAPI
- **Gerenciador de Dependências**: Poetry
- **API**: Bling API V3
- **Orquestração de Contêineres**: Docker Compose

## 📒 Estrutura do Projeto
```plaintext
.
C:.
├───app
│   ├───models
│   ├───routes
│   │   ├───bling
│   │   ├───logs
│   ├───services
├── __main.py                # Arquivo principal da API
├── pyproject.toml         # Configuração do Poetry
├── poetry.lock            # Dependências travadas
├── requirements.txt       # Dependências para ambientes sem Poetry
├── compose.yaml           # Configuração do Docker Compose
├── Dockerfile             # Imagem Docker para a aplicação
├── README.md              # Documentação do projeto
└── .env                   # Variáveis de ambiente (ignorado por padrão)
```

## 🔗 Como Configurar e Executar

### 1. Clonar o Repositório
```bash
git clone ...
cd ...
```

### 2. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
BLING_CLIENT_ID=client_id
BLING_CLIENT_SECRET=client_secret
BLING_TOKEN_URL=token_url
BLING_BASE_URL=base_url
BLING_ACCESS_TOKEN=access_token
BLING_REFRESH_TOKEN=refresh_token

```

### 3. Instalar Dependências
#### Usando Poetry:
```bash
poetry install
```
#### Usando pip (alternativo):
```bash
pip install -r requirements.txt
```

### 4. Executar Localmente
#### Com Uvicorn:
```bash
uvicorn __main:app --host 0.0.0.0 --port 8000
```

### 5. Executar com Docker
#### Build e Execução:
```bash
docker-compose up --build
```

## ⚡ Endpoints Disponíveis

### GET `/products/search`
Faz busca geral de  produtos

### GET `/logs`
Recebe os logs gerais da API


## 🛠️ Contribuições
Contribuições são bem-vindas! Por favor, abra um PR ou uma issue para discussão.

## ✨ Autor
- **André Luiz Montanha**  
  E-mail: [alm28062001@gmail.com](mailto:alm28062001@gmail.com)

## 🌐 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.

---
Vamos transformar a comunicação automática com WhatsApp em algo incrível! 🚀
