from pydantic import BaseModel

#Request model for session creation
class SessionRequest(BaseModel):
    user_id: str


