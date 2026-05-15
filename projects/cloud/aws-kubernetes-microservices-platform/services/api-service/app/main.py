from fastapi import FastAPI, Depends
from app.security import verify_token
from app.models import Note

app = FastAPI(
    title="API Service",
    version="1.0.0"
)

fake_notes_db = []


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/notes")
def get_notes(user=Depends(verify_token)):
    return {
        "notes": fake_notes_db,
        "user": user
    }


@app.post("/notes")
def create_note(
    note: Note,
    user=Depends(verify_token)
):
    fake_notes_db.append(note.dict())

    return {
        "message": "Note created",
        "note": note,
        "user": user
    }