from sqlalchemy.ext.asyncio import AsyncSession
from application.repositories.task_repositories import get_task, add_task, get_tasks, del_task
from application.shcemas.tasks_dto import CreateTask, ReadTask, BaseTask


async def check_tasks(session : AsyncSession):
    tasks = await get_tasks(session)
    if tasks:
        return tasks
    raise ValueError("Задачи не найдены")

async def check_task(session : AsyncSession, title : str):
    task = await get_task(session, title)
    if task:
        return task
    raise ValueError("Задача не найдена")

async def create_task(session : AsyncSession, task_data : CreateTask):
    task = await get_task(session, task_data.title)
    if task:
        raise ValueError("Задача уже существует")
    await add_task(session, task_data)

async def remove_task(session : AsyncSession, title : str):
    task = await get_task(session, title)
    if task:
        await del_task(session, title)
    raise ValueError("Задача не найдена")