from application.utils.setup import setup_db
from application.models import TaskORM
from datetime import date
import pytest
from application.core.connection import session

tasks = [TaskORM(title = "test1", description = "test1", status = "done", deadline = date(year =2025, month=5, day= 3),
                 created_at =date(year =2025, month=4, day= 2)),
         TaskORM(title="test2", description="test2", status="running", deadline=date(year=2025, month=5, day=20),
                 created_at=date(year=2025, month=5, day=9)),
         TaskORM(title="test3", description="test3", status="done", deadline=date(year=2025, month=5, day=19),
                 created_at=date(year=2025, month=5, day=1)),
         ]

@pytest.fixture(autouse=True)
async def setup_environment():

    await setup_db()

    async with session.begin() as sess:
        sess.add_all(tasks)

    yield
