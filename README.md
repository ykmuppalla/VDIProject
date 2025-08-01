# VDI Session Broker

A RESTful API for managing Virtual Desktop Infrastructure (VDI) sessions.

## Features

- Create VDI sessions with unique session IDs
- Retrieve session status
- Terminate sessions
- Thread-safe session management
- Comprehensive unit tests
- Containerized deployment with Docker
- Production-ready configuration

## API Endpoints

### POST /sessions
Creates a new VDI session.

**Request:**
```json
{
  "user_id": "john_doe"
}
```

**Response:**
```json
{
  "session_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": "john_doe",
  "desktop_url": "https://vdi.tiktok.com/desktop/123e4567-e89b-12d3-a456-426614174000",
  "status": "pending",
  "created_at": "2024-01-01T12:00:00"
}
```

### GET /sessions/{session_id}
Retrieves the status of a specific session.

**Response:**
```json
{
  "status": "active"
}
```

### DELETE /sessions/{session_id}
Terminates a session.

**Response:**
```json
{
  "message": "Session terminated"
}
```

## Running the Application

### Using Docker (Recommended)

```bash
# Build and run with docker-compose
docker-compose up --build

# Or build and run manually
docker build -t session-broker .
docker run -p 8000:8000 session-broker
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

### Access API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Running Tests

```bash
# Local testing
python -m pytest unittests/ -v

# Testing in Docker
docker build -t session-broker .
docker run session-broker python -m pytest unittests/ -v
```

