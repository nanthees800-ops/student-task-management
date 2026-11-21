from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.task_manager import TaskManager

app = FastAPI(
    title="Student Task Management System",
    description="DevOps Integrated Practical Project",
    version="1.0"
)

manager = TaskManager()


class TaskRequest(BaseModel):
    student_name: str = Field(min_length=1)
    student_id: str = Field(min_length=1)
    title: str = Field(min_length=1)


class StatusRequest(BaseModel):
    status: str


@app.get("/")
def home():
    return {"message": "Student Task Management API is running"}


@app.post("/tasks")
def add_task(request: TaskRequest):
    try:
        return manager.add_task(
            request.student_name,
            request.student_id,
            request.title
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.get("/tasks")
def get_all_tasks():
    return manager.get_all_tasks()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return manager.get_task(task_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.put("/tasks/{task_id}")
def update_task(task_id: int, request: StatusRequest):
    try:
        return manager.update_status(task_id, request.status)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        return manager.delete_task(task_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.get("/students/{student_id}/tasks")
def search_student_tasks(student_id: str):
    return manager.search_by_student(student_id)
