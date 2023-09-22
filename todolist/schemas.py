from pydantic import BaseModel
from typing import List, Optional
# By organizing your models in this way, you achieve several benefits:
#
# Code Reuse: You define the common fields once in TaskBase and then extend it
# for more specialized use cases (e.g., Task for ORM operations and TaskCreate for creating tasks).
#
# Clarity: The code is more organized and self-explanatory, making it easier for
# developers to understand the purpose of each model.
#
# Flexibility: If you need to make changes or add fields in the future, you only
# need to update one place (e.g., TaskBase) instead of multiple places.
#
# Configuration: You can use the Config class to fine-tune how Pydantic handles these models.
# In this case, you enable orm_mode for the Task model, indicating it's suitable for use with an ORM (e.g., SQLAlchemy).
class TaskBase(BaseModel):
    text: str

class Task(TaskBase):
    id: str
    user_id: str

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass

class UserBase(BaseModel):
    username: str
    email: str
    name: str
    hashed_password: str

class User(UserBase):
    id: str
    tasks: List[Task] = []

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass