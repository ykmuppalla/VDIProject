import uuid
from threading import Lock
from datetime import datetime
from typing import Dict, Union

from datamodels.session import Session
from datamodels.sessionResponse import SessionResponse
from datamodels.sessionStatus import SessionStatus


class SessionManager:

    def __init__(self):
        self.sessions: Dict[str, Session] = {}
        self._lock = Lock()  # Thread safety

    def create_session(self, user_id: str) -> SessionResponse:
        session_id = str(uuid.uuid4())
        desktop_url = f"https://vdi.tiktok.com/desktop/{session_id}"

        session = Session(
            session_id=session_id,
            user_id=user_id,
            desktop_url=desktop_url,
            status=SessionStatus.PENDING,
            created_at=datetime.now()
        )

        with self._lock:
            self.sessions[session_id] = session
        # TODO: Persist session to database and create any resources
        self.update_session_status(session_id, SessionStatus.ACTIVE)

        return SessionResponse(**session.model_dump())

    #Not exposed to customer
    def get_session(self, session_id: str) -> Union[Session, None]:
        with self._lock:
            return self.sessions.get(session_id)

    def get_session_status(self, session_id: str) -> Union[SessionStatus, None]:
        session = self.sessions.get(session_id)
        return session.status if session else None

    def delete_session(self, session_id: str) -> bool:
        #TODO clean up resources related to sessions
        return self.update_session_status(session_id, SessionStatus.TERMINATED)

    def update_session_status(self, session_id: str, new_status: SessionStatus) -> bool:
        with self._lock:
            if session_id in self.sessions:
                self.sessions[session_id].status = new_status
                # TODO: Update database
                return True
            return False

    #Not in requirements
    def clean_up_expired_sessions(self):
        pass

    def __str__(self):
        return f"SessionManager with {len(self.sessions)} active sessions"