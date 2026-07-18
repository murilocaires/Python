# Desenvolvimento com Flask

Esta pasta contém projetos de estudo relacionados ao framework Flask, com foco em criação de aplicações web e APIs REST.

## Projetos disponíveis

### CRUD de atividades
Aplicação simples em Flask para cadastrar, listar, atualizar e excluir tarefas. A API funciona com uma estrutura em memória, o que torna o exemplo ideal para aprender os conceitos básicos de rotas, requisições e respostas JSON.

### Banco de dados e autenticação
Projeto intermediário que explora integração com banco de dados, autenticação de usuários e proteção de senhas.

### API do Pix (comunicação em tempo real)
Aplicação Flask que simula um fluxo de cobrança via PIX com geração de QR Code, confirmação de pagamento e atualização em tempo real para o cliente por meio de WebSockets com Socket.IO.

## Como executar
1. Entre na pasta do projeto desejado:

```bash
cd "1 CRUD de atividades"
```

ou

```bash
cd "3 Comunicação em tempo real com Flask (PIX)"
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python app.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

## Conceitos praticados
- criação de rotas com Flask;
- uso de métodos HTTP como GET, POST, PUT e DELETE;
- retorno de dados em formato JSON;
- integração com banco de dados;
- comunicação em tempo real com Flask-SocketIO;
- estruturação básica de projetos com módulos.
