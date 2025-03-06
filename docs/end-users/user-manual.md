### 2. Documento para Usuário Final

# Manual do Usuário - Task Manager API

## Introdução
Bem-vindo ao Task Manager API! Este é um sistema simples para criar, listar, atualizar e excluir tarefas. Este manual explica como usar a API.

## Como Usar
Acesse a interface em `http://127.0.0.1:8000/docs` após iniciar a aplicação. Você verá os seguintes recursos:

### Criar uma Tarefa
- **Endpoint**: `POST /tasks/`
- **Exemplo**: Envie um JSON como:
  ```json
  {
    "id": 1,
    "title": "Reunião",
    "description": "Planejar sprint",
    "completed": false
  }
    ```
- Resultado: A tarefa é adicionada à lista.

### Listar Tarefas
- Endpoint: GET /tasks/
- Resultado: Retorna todas as tarefas criadas.

### Atualizar uma Tarefa
- Endpoint: PUT /tasks/{id}
- Exemplo: Atualize a tarefa com ID 1:
```json
    {
      "id": 1,
      "title": "Reunião Atualizada",
      "description": "Planejar sprint com equipe",
      "completed": false
    }
```