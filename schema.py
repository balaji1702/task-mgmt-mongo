from pydantic import BaseModel
from enum_ import Priority,Status


class Task(BaseModel):
    task_name: str
    description: str  
    priority :Priority
    status: Status