import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_session():
    response = client.post("/sessions", json={"user_id": "test_user"})
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert "desktop_url" in data
    assert data["user_id"] == "test_user"
    assert data["status"] == "active"

def test_create_session_empty_user_id():
    response = client.post("/sessions", json={"user_id": ""})
    assert response.status_code == 400
    assert "user_id is required" in response.json()["detail"]

def test_get_session():
    # Create session first
    create_response = client.post("/sessions", json={"user_id": "test_user"})
    session_id = create_response.json()["session_id"]
    
    # Get session
    response = client.get(f"/sessions/{session_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_get_session_not_found():
    response = client.get("/sessions/nonexistent-id")
    assert response.status_code == 404
    assert "Session not found" in response.json()["detail"]

def test_get_session_empty_id():
    response = client.get("/sessions/")
    assert response.status_code == 405  # Method Not Allowed for trailing slash

def test_delete_session():
    # Create session first
    create_response = client.post("/sessions", json={"user_id": "test_user"})
    session_id = create_response.json()["session_id"]
    
    # Delete session
    response = client.delete(f"/sessions/{session_id}")
    assert response.status_code == 200
    assert "Session terminated" in response.json()["message"]

def test_delete_session_not_found():
    response = client.delete("/sessions/nonexistent-id")
    assert response.status_code == 404
    assert "Session not found" in response.json()["detail"]