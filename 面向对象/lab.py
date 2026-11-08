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

