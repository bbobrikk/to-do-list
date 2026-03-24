from fastapi import APIRouter, HTTPException
from application.services.task_services import (
    check_task,
    check_tasks,
    create_task,
    remove_task,
    complete_task,
)
from application.utils.dependency import SessionDep
from application.shcemas.tasks_dto import CreateTask, BaseTask, ReadTask


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/{title}", response_model=list[ReadTask])
async def get_task(session: SessionDep, title: str):
    try:
        tasks = await check_task(session, title)
        return tasks
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@router.get("", response_model=list[BaseTask])
async def get_tasks(session: SessionDep):
    try:
        task = await check_tasks(session)
        return task
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@router.post("")
async def add_task(session: SessionDep, task_data: CreateTask):
    try:
        await create_task(session, task_data)
        return {"status": "Задача создана"}
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@router.delete("/{title}")
async def del_task(session: SessionDep, title: str):
    try:
        await remove_task(session, title)
        return {"status": "Задача удалена"}
    except ValueError as er:
        raise HTTPException(status_code=404, detail=str(er))


@router.put("/{title}")
async def change_status(session: SessionDep, title: str):
    try:
        await complete_task(session, title)
        return {"status": "Задача завершена"}
    except ValueError as er:
        raise HTTPException(status_code=422, detail=str(er))
