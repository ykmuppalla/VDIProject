from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from datamodels.sessionStatus import SessionStatus


#Object Model used to persist in the DataBase
class Session(BaseModel):
    session_id: str
    user_id: str
    desktop_url: str
    status: SessionStatus
    created_at: datetime
    expired_at: Optional[datetime] = None
