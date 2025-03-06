### 4. Documento de Integração de API

# Guia de Integração de API - Task Manager API

## Introdução
Este guia é para desenvolvedores ou sistemas que desejam integrar-se à Task Manager API.

## Base URL
- `http://127.0.0.1:8000` (local) ou URL fornecida pelo deploy.

## Endpoints Disponíveis
### 1. Criar Tarefa
- **Método**: `POST`
- **Rota**: `/tasks/`
- **Cabeçalho**: `Content-Type: application/json`
- **Corpo**:
  ```json
  {
    "id": 1,
    "title": "Nova Tarefa",
    "description": "Descrição aqui",
    "completed": false
  }
    ```