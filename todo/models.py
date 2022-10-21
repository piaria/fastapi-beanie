from beanie import Document
from pydantic import BaseModel, Field


class Todo(Document):
    completed: bool = False
    task: str = Field(...)
