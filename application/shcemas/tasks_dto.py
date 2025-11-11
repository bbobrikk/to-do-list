from datetime import date

from pydantic import BaseModel

class BaseTask(BaseModel):
    title : str
    description : str

class CreateTask(BaseTask):
    deadline : date
    created_at : date

class ReadTask(CreateTask):
    task_id : int