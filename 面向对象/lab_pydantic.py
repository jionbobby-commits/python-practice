from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    name: str = Field(max_length=10)
    remark: str = ""

b = BookCreate(name="三体")
print(b)
print(b.name)
print(b.model_dump())