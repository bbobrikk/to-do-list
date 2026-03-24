from datetime import date
from httpx import AsyncClient, ASGITransport
from application.main import app


class TestTasks:

    async def test_get_tasks(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("tasks")
            assert response.status_code == 200 and len(response.json()) == 3

    async def test_get_task(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            response = await client.get("tasks/test1")
            assert (
                response.status_code == 200 and response.json()[0]["title"] == "test1"
            )

    async def test_add_task(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            task = {
                "title": "test4",
                "description": "test4",
                "deadline": date(year=2025, month=5, day=19).isoformat(),
                "created_at": date(year=2025, month=5, day=1).isoformat(),
            }
            await client.post("tasks", json=task)
            response = await client.get("tasks")
            assert response.status_code == 200 and len(response.json()) == 4

    async def test_del_task(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            await client.delete("/tasks/test1")
            response = await client.get("/tasks")
            assert response.status_code == 200 and len(response.json()) == 2

    async def test_complete_task(self):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as client:
            await client.put("/tasks/test2")
            response = await client.get("/tasks/test2")
            assert (
                response.status_code == 200 and response.json()[0]["status"] == "done"
            )
