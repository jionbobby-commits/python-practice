from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"msg": "你好"}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    return {"note_id": note_id}


from pydantic import field_validator

@field_validator("name")
@classmethod
def check_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("书名不能为空白")
        return v

@field_validator("shelf")
@classmethod
def check_shelf(cls, v: str) -> str:
        v = v.strip()
        if not v:
            return "未分类"
        return v

from pydantic import field_validator

@field_validator("name")
@classmethod
def check_name(cls, v: str) -> str:
    v = v.strip()
    if not v:
        raise ValueError("书名不能为空白")
    return v

@classmethod
def check_shelf(cls, v: str) -> str:
        v = v.strip()
        if not v:
            return "未分类"
        return v

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.0",port=8000)