# Student Task Management System

## Project Description
A Python REST API for managing student assignments.

## Technologies
- Python
- FastAPI
- Pytest
- Git and GitHub
- Docker
- Terraform

## Features
- Add student tasks
- View all tasks
- Update task status
- Delete tasks
- Search student tasks

## Install
```bash
pip install -r requirements.txt
```

## Run locally
```bash
uvicorn app.main:app --reload
```

## Test
```bash
pytest -v
```

## Coverage
```bash
pytest --cov=app --cov-report=html
```

## Docker
```bash
docker build -t student-task-app:v1 .
docker run -d -p 8000:8000 student-task-app:v1
```

## Terraform
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
