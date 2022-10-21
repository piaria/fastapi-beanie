from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from todo.exceptions import DomainException
from todo.models import Todo

api = APIRouter(prefix="/todos")


async def get_todo(id: PydanticObjectId) -> Todo:
    todo = await Todo.get(id)
    if todo is None:
        raise DomainException("Todo not found")
    return todo


@api.get("/", response_model=List[Todo])
async def get_todos():
    return await Todo.find_all().to_list()


@api.post("/", response_model=Todo)
async def add_todos(todo: Todo):
    return await todo.create()


@api.put("/{id}/toggle_complete", response_model=Todo)
async def complete_todo(todo: Todo = Depends(get_todo)):
    todo.completed = not todo.completed
    await todo.save()
    return todo


@api.delete("/{id}")
async def delete_todo(todo: Todo = Depends(get_todo)):
    await todo.delete()
    return "OK"
