### 3. Documento de Modelagem de Banco de Dados

# Modelagem de Banco de Dados - Task Manager API

## Visão Geral
Atualmente, o Task Manager API usa uma lista em memória para armazenar tarefas. Este documento descreve a modelagem proposta para um futuro banco de dados relacional (SQLite).

## Esquema Proposto
### Tabela: `tasks`
| Coluna        | Tipo         | Descrição                     | Chave Primária |
|---------------|--------------|-------------------------------|----------------|
| `id`          | INTEGER      | Identificador único da tarefa | Sim            |
| `title`       | TEXT         | Título da tarefa             | Não            |
| `description` | TEXT         | Descrição da tarefa          | Não            |
| `completed`   | BOOLEAN      | Status de conclusão          | Não            |

## Exemplo de SQL
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (title, description, completed) VALUES
    ('Reunião', 'Planejar sprint', FALSE);
```