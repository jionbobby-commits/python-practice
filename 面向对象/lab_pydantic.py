from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    name: str = Field(max_length=10)
    remark: str = ""

b = BookCreate(name="三体")
print(b)
print(b.name)
print(b.model_dump())

@app.get("/books", response_model=BookPage)
def list_books(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
):
    ordered = sorted(books, key=lambda b: (b["updated_at"], b["id"]), reverse=True)
    start = (page - 1) * page_size
    return {
        "items": ordered[start : start + page_size],
        "total": len(books),
        "page": page,
        "page_size": page_size,
    }

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


@app.get("/books", response_model=BookPage)
def list_books(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
):
    ordered = sorted(books, key=lambda b: (b["updated_at"], b["id"]), reverse=True)
    start = (page - 1) * page_size
    return {
        "items": ordered[start : start + page_size],
        "total": len(books),
        "page": page,
        "page_size": page_size,
    }


# !/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()