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
