from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
import markdown
import os

# Inicializa o FastAPI
app = FastAPI(title="Task Manager API")

# Modelo para as tarefas
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# Banco de dados simulado (lista em memória)
tasks_db: List[Task] = []

# Rota para criar uma tarefa (POST)
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    for existing_task in tasks_db:
        if existing_task.id == task.id:
            raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks_db.append(task)
    return task

# Rota para listar todas as tarefas (GET)
@app.get("/tasks/", response_model=List[Task])
async def list_tasks():
    return tasks_db

# Rota para atualizar uma tarefa (PUT)
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            if updated_task.id != task_id:
                raise HTTPException(status_code=400, detail="Task ID cannot be changed")
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Rota para marcar tarefa como concluída (PATCH)
@app.patch("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i].completed = True
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Task not found")

# Rota para deletar uma tarefa (DELETE)
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# Rota inicial
@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}

# Função para ler e converter Markdown em HTML
def read_markdown_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Document not found")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return markdown.markdown(content)

# Rota para listar todos os documentos disponíveis
@app.get("/docs/", response_model=List[str])
async def list_docs():
    doc_dirs = ["developers", "end-users", "database", "api-integration"]
    docs_list = []
    for directory in doc_dirs:
        dir_path = os.path.join("docs", directory)
        if os.path.exists(dir_path):
            files = [f.replace(".md", "") for f in os.listdir(dir_path) if f.endswith(".md")]
            docs_list.extend([f"{directory}/{file}" for file in files])
    return docs_list

# Rota para exibir um documento específico como HTML
@app.get("/docs/{doc_path:path}", response_class=HTMLResponse)
async def get_doc(doc_path: str):
    file_path = os.path.join("docs", f"{doc_path}.md")
    html_content = read_markdown_file(file_path)
    # Estilização básica para o HTML
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Manager Docs - {doc_path}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return HTMLResponse(content=html_template)