from pydantic import BaseModel, Field, field_validator


class Demo(BaseModel):
    title: str = Field(max_length=10)
    content: str = ""

    @field_validator("title")
    @classmethod
    def check_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("标题不能为空白")
        return v


d = Demo(title="  你好  ")
print(d.title)
print(d.model_dump())

from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException

from app.schemas import NoteCreate, NoteRead

app = FastAPI(title="FastAPI Notes")

notes = []
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/notes", response_model=NoteRead, status_code=201)
def create_note(data: NoteCreate):
    global next_id
    now = datetime.now(timezone.utc)
    note = {
        "id": next_id,
        **data.model_dump(),
        "is_favorite": False,
        "created_at": now,
        "updated_at": now,
    }
    notes.append(note)
    next_id += 1
    return note