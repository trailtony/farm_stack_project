from pydantic import BaseModel

class Todo(BaseException):
    title: str
    description: str