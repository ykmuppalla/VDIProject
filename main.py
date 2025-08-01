from fastapi import FastAPI, HTTPException
from datamodels.sessionRequest import SessionRequest
from datamodels.sessionResponse import SessionResponse
from handlers.sessionManager import SessionManager

app = FastAPI(title="VDI Session Broker")
session_manager = SessionManager()


@app.post('/sessions', response_model=SessionResponse)
async def create_session(request: SessionRequest):
    if not request.user_id or not request.user_id.strip():
        raise HTTPException(status_code=400, detail="user_id is required")
    return session_manager.create_session(request.user_id.strip())


@app.get('/sessions/{session_id}')
async def get_session(session_id: str):
    if not session_id or not session_id.strip():
        raise HTTPException(status_code=400, detail="session_id is required")
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"status": session.status}


@app.delete('/sessions/{session_id}')
async def delete_session(session_id: str):
    if not session_id or not session_id.strip():
        raise HTTPException(status_code=400, detail="session_id is required")
    success = session_manager.delete_session(session_id)
    if not success:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"message": "Session terminated"}
