import os

os.environ["DATABASE_URL"] = "sqlite:///./test_tasks.db"

from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create_and_get_tasks():
    payload = {
        "title": "Read React docs",
        "description": "Finish the assignment before Friday.",
        "status": "PENDING",
        "priority": "HIGH",
    }

    create_response = client.post("/api/tasks", json=payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["title"] == payload["title"]
    assert created["status"] == payload["status"]

    list_response = client.get("/api/tasks")
    assert list_response.status_code == 200
    assert len(list_response.json()) >= 1


def test_update_task_and_search_filter():
    task = client.post(
        "/api/tasks",
        json={
            "title": "Write report",
            "description": "Prepare the daily summary",
            "status": "PENDING",
            "priority": "MEDIUM",
        },
    ).json()

    update_response = client.put(
        f"/api/tasks/{task['id']}",
        json={"status": "COMPLETED", "priority": "HIGH"},
    )
    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["status"] == "COMPLETED"
    assert updated["priority"] == "HIGH"

    search_response = client.get("/api/tasks?search=report")
    assert search_response.status_code == 200
    assert any(item["id"] == task["id"] for item in search_response.json())

    status_response = client.get("/api/tasks?status=COMPLETED")
    assert status_response.status_code == 200
    assert all(item["status"] == "COMPLETED" for item in status_response.json())


def test_invalid_task_id_and_validations():
    missing = client.get("/api/tasks/999999")
    assert missing.status_code == 404

    empty_title = client.post("/api/tasks", json={"title": "   ", "status": "PENDING", "priority": "LOW"})
    assert empty_title.status_code == 422

    bad_status = client.post("/api/tasks", json={"title": "Bad status", "status": "FAILED", "priority": "LOW"})
    assert bad_status.status_code == 422

    bad_priority = client.post("/api/tasks", json={"title": "Bad priority", "status": "PENDING", "priority": "URGENT"})
    assert bad_priority.status_code == 422


def test_delete_task():
    task = client.post(
        "/api/tasks",
        json={"title": "Delete me", "status": "PENDING", "priority": "LOW"},
    ).json()

    delete_response = client.delete(f"/api/tasks/{task['id']}")
    assert delete_response.status_code == 204

    fetch_after_delete = client.get(f"/api/tasks/{task['id']}")
    assert fetch_after_delete.status_code == 404
