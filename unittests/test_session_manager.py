import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from handlers.sessionManager import SessionManager
from datamodels.sessionStatus import SessionStatus

def test_create_session():
    manager = SessionManager()
    session = manager.create_session("test_user")
    
    assert session.user_id == "test_user"
    assert session.session_id is not None
    assert session.desktop_url.startswith("https://vdi.tiktok.com/desktop/")
    assert session.status == SessionStatus.ACTIVE
    assert session.created_at is not None

def test_get_session():
    manager = SessionManager()
    created_session = manager.create_session("test_user")
    
    retrieved_session = manager.get_session(created_session.session_id)
    assert retrieved_session is not None
    assert retrieved_session.session_id == created_session.session_id
    assert retrieved_session.user_id == "test_user"

def test_get_session_not_found():
    manager = SessionManager()
    session = manager.get_session("nonexistent-id")
    assert session is None

def test_delete_session():
    manager = SessionManager()
    created_session = manager.create_session("test_user")
    
    success = manager.delete_session(created_session.session_id)
    assert success is True
    
    # Check session is terminated
    session = manager.get_session(created_session.session_id)
    assert session.status == SessionStatus.TERMINATED

def test_delete_session_not_found():
    manager = SessionManager()
    success = manager.delete_session("nonexistent-id")
    assert success is False