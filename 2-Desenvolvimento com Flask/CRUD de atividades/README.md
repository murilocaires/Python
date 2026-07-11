# CRUD de atividades com Flask

Este projeto é uma API simples em Flask para gerenciar uma lista de tarefas. Ele foi desenvolvido como exemplo de estudo para praticar operações básicas de CRUD (Criar, Ler, Atualizar e Excluir).

## Funcionalidades

A aplicação permite:
- cadastrar uma nova tarefa;
- listar todas as tarefas;
- consultar uma tarefa específica;
- atualizar uma tarefa;
- remover uma tarefa.

## Estrutura do projeto

- app.py: arquivo principal com as rotas e a execução da aplicação.
- models/task.py: modelo da tarefa.
- requirements.txt: dependências do projeto.

## Endpoints disponíveis

### Criar tarefa
- Método: POST
- Rota: /tasks
- Corpo esperado (JSON):

```json
{
  "title": "Estudar Flask",
  "description": "Revisar rotas e APIs"
}
```

### Listar tarefas
- Método: GET
- Rota: /tasks

### Buscar tarefa por ID
- Método: GET
- Rota: /tasks/<id>

### Atualizar tarefa
- Método: PUT
- Rota: /tasks/<id>

### Excluir tarefa
- Método: DELETE
- Rota: /tasks/<id>

## Como executar

1. Entre na pasta do projeto:

```bash
cd "CRUD de atividades"
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
Os dados são armazenados em memória durante a execução da aplicação. Ou seja, ao reiniciar o servidor, as tarefas cadastradas serão perdidas.
