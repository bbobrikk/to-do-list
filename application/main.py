from contextlib import asynccontextmanager
from application.utils.setup import setup_db
from fastapi import FastAPI
from uvicorn import run
from application.apies.task_apies import router


@asynccontextmanager
async def lifespan(app: FastAPI):

    await setup_db()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == "__main__":
    run("main:app")
