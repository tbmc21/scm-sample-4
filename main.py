from fastapi import FastAPI, HTTPException
from typing import List, Dict
from pydantic import BaseModel

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
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Rota para deletar uma tarefa (DELETE)
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# Rota inicial para teste
@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}