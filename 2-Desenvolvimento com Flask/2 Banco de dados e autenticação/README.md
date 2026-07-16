# Banco de dados e autenticação com Flask

Este projeto é uma API simples em Flask para gerenciar usuários com autenticação e autorização básica. Ele foi desenvolvido como exemplo de estudo para praticar operações de CRUD (Criar, Ler, Atualizar e Excluir) em conjunto com login, logout, roles e criptografia de senha usando Flask-Login, SQLAlchemy e bcrypt.

## Funcionalidades

A aplicação permite:
- cadastrar um novo usuário;
- fazer login com autenticação segura;
- fazer logout;
- listar usuários;
- consultar um usuário específico;
- atualizar a senha de um usuário;
- remover um usuário, respeitando regras de permissão;
- utilizar roles como `user` e `admin`.

## Estrutura do projeto

- app.py: arquivo principal com as rotas, autenticação, autorização e execução da aplicação.
- database.py: configuração do banco de dados SQLAlchemy.
- models/user.py: modelo do usuário.
- requirements.txt: dependências do projeto.
- instance/database.db: banco SQLite gerado automaticamente.

## Endpoints disponíveis

### Cadastrar usuário
- Método: POST
- Rota: /user
- Corpo esperado (JSON):

```json
{
  "username": "alice",
  "password": "123456",
  "role": "user"
}
```

### Listar usuários
- Método: GET
- Rota: /user

### Buscar usuário por ID
- Método: GET
- Rota: /user/<id>

### Atualizar senha
- Método: PUT
- Rota: /user/<id>
- Corpo esperado (JSON):

```json
{
  "password": "nova_senha"
}
```

### Excluir usuário
- Método: DELETE
- Rota: /user/<id>
- Regras: apenas usuários com role `admin` podem remover outros usuários.

### Fazer login
- Método: POST
- Rota: /login
- Corpo esperado (JSON):

```json
{
  "username": "alice",
  "password": "123456"
}
```

### Fazer logout
- Método: GET
- Rota: /logout

## Segurança

- As senhas são armazenadas com hash utilizando bcrypt.
- A validação de login compara a senha fornecida com o hash salvo no banco.
- A rota de atualização e exclusão verifica se o usuário autenticado possui permissão para executar a ação.

## Como executar

1. Entre na pasta do projeto:

```bash
cd "2 Banco de dados e autenticação"
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie a aplicação:

```bash
python app.py
```

A aplicação será iniciada em modo de depuração e poderá ser acessada em:

```text
http://127.0.0.1:5000
```

## Observação
Os dados são armazenados em um banco SQLite localizado na pasta instance, então permanecem entre execuções do servidor.
