import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks():
    from app.main import manager
    manager.tasks.clear()
    manager.next_id = 1


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_task():
    response = client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python Assignment"
    })
    assert response.status_code == 200
    assert response.json()["student_name"] == "Arun"


def test_add_task_empty_name():
    response = client.post("/tasks", json={
        "student_name": "",
        "student_id": "ST101",
        "title": "Python Assignment"
    })
    assert response.status_code == 422


def test_add_task_empty_title():
    response = client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": ""
    })
    assert response.status_code == 422


def test_get_all_tasks():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_task():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_update_status():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.put(
        "/tasks/1",
        json={"status": "Completed"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "Completed"


def test_invalid_status():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.put(
        "/tasks/1",
        json={"status": "Started"}
    )
    assert response.status_code == 400


def test_delete_task():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.delete("/tasks/1")
    assert response.status_code == 200


def test_delete_nonexistent_task():
    response = client.delete("/tasks/999")
    assert response.status_code == 404


def test_search_student():
    client.post("/tasks", json={
        "student_name": "Arun",
        "student_id": "ST101",
        "title": "Python"
    })
    response = client.get("/students/ST101/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 1
