from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"msg": "你好"}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    return {"note_id": note_id}