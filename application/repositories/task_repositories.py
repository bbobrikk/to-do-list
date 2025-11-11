from sqlalchemy.ext.asyncio import AsyncSession
from application.models import TaskORM
from sqlalchemy import select
from application.shcemas.tasks_dto import CreateTask


async def get_tasks(session : AsyncSession):
    query = select(TaskORM)
    result = await session.execute(query)
    return result.scalars().all()

async def get_task(session : AsyncSession, title : str):
    query = select(TaskORM).filter(TaskORM.title == title)
    result = await session.execute(query)
    return result.scalars().all()

async def add_task(session : AsyncSession, task_data : CreateTask):
    task = TaskORM(title = task_data.title,
                   description = task_data.description,
                   created_at = task_data.created_at,
                   deadline = task_data.deadline)
    session.add(task)

async def del_task(session : AsyncSession, title : str):
    task = await get_task(session, title)
    await session.delete(task)
