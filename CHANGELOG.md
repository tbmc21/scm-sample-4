# Changelog

Todas as mudanças significativas neste projeto serão registradas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), e usamos [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Planejado: Adicionar persistência de dados com SQLite.

## [1.1.1] - 2025-03-06
### Fixed
- Resolvido bug no endpoint DELETE que não retornava mensagem correta em caso de tarefa inexistente.

## [1.1.0] - 2025-03-05
### Added
- Endpoint PATCH `/tasks/{task_id}/complete` para alterar o status de conclusão de tarefas.

### Changed
- Melhorada a validação no endpoint PUT para evitar alterações no ID.

## [1.0.1] - 2025-03-03
### Added
- Adicionado após as rotas existentes

## [1.0.0] - 2025-03-04
### Added
- API inicial com endpoints CRUD:
  - POST `/tasks/` - Criar tarefa.
  - GET `/tasks/` - Listar tarefas.
  - PUT `/tasks/{task_id}` - Atualizar tarefa.
  - DELETE `/tasks/{task_id}` - Excluir tarefa.
- Rota raiz GET `/` com mensagem de boas-vindas.

### Notes
- Versão inicial marcada como estável para demonstração de SCM.