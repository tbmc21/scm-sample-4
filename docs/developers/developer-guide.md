# Guia do Desenvolvedor - Task Manager API

## Visão Geral
Este documento é destinado aos desenvolvedores que trabalham na Task Manager API, uma aplicação baseada em FastAPI para gerenciamento de tarefas.

## Pré-requisitos
- Python 3.9+
- Dependências: `fastapi`, `uvicorn` (instale via `pip install fastapi uvicorn`)

## Estrutura do Código
- **`main.py`**: Arquivo principal contendo a lógica da API.
  - Endpoints: CRUD básico + funcionalidade de conclusão de tarefas.
  - Banco de dados: Lista em memória (futuro: SQLite).

## Como Executar
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd task_manager
   ```

2. Instale as dependências:
```bash
  pip install -r requirements.txt  # Crie este arquivo se necessário
```

3. Inicie a API:
```bash
  uvicorn main:app --reload
```

4. Acesse a documentação interativa em: http://127.0.0.1:8000/docs

### Fluxo de Desenvolvimento
- Crie uma branch para novas funcionalidades: git checkout -b feature/nome-da-funcionalidade.
- Faça commits atômicos: git commit -m "Descrição clara da mudança".
- Atualize o CHANGELOG.md antes de criar uma tag de versão.

### Próximos Passos
- Implementar persistência com SQLite.
- Adicionar autenticação de usuários.
- 
### Contribuição
- Siga o padrão de pull requests no GitHub e documente todas as alterações no CHANGELOG.md.