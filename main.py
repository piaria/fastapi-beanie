from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from todo import models as todo_models
from todo.exceptions import DomainException
from todo.routers import api as todo_api

app = FastAPI()

app.include_router(todo_api)


@app.on_event("startup")
async def init_my_beanie():
    client = AsyncIOMotorClient(settings.MONGODB_URL)[settings.SERVICE_DB]
    # Init beanie with
    await init_beanie(database=client, document_models=todo_models)


@app.exception_handler(DomainException)
async def validation_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content=exc.args,
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}
