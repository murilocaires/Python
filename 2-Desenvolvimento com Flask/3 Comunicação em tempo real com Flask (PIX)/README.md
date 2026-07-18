# API do Pix com comunicação em tempo real

Este projeto é uma aplicação Flask que simula um fluxo de pagamento via PIX com confirmação em tempo real. A ideia é demonstrar o uso de:

- Flask para criar uma API web;
- Flask-SocketIO para comunicação em tempo real;
- SQLAlchemy para persistência dos pagamentos;
- geração de QR Code para representar a cobrança PIX.

## Funcionalidades

- criação de uma cobrança PIX via endpoint HTTP;
- geração de QR Code associado ao pagamento;
- renderização da página de pagamento com o QR Code;
- confirmação do pagamento por um endpoint de callback;
- atualização em tempo real para o cliente via WebSocket.

## Estrutura do projeto

- app.py: configuração da aplicação e rotas principais;
- payments/pix.py: lógica para criar dados de pagamento PIX;
- db_models/payments.py: modelo da entidade Payment;
- repository/database.py: configuração do banco de dados;
- templates/: páginas HTML para pagamento e confirmação;
- static/: arquivos estáticos e imagens geradas.

## Como executar

1. Entre na pasta do projeto:

```bash
cd "3 Comunicação em tempo real com Flask (PIX)"
```

2. Crie e ative um ambiente virtual, se desejar:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse a aplicação no navegador:

```text
http://127.0.0.1:5000
```

## Endpoints principais

- POST /payments/pix: cria uma cobrança PIX;
- GET /payments/pix/qr_code/<file_name>: retorna a imagem do QR Code;
- GET /payments/pix/<payment_id>: exibe a página de pagamento;
- POST /payments/pix/confirmation: confirma o pagamento.

## Conceitos abordados

- APIs REST com Flask;
- comunicação assíncrona com WebSockets;
- integração com banco de dados relacional;
- manipulação de arquivos de imagem para QR Code;
- fluxo básico de pagamento e confirmação.
