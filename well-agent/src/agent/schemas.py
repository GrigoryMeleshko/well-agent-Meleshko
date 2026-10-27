"""Pydantic-схемы: задача, результат, журнал."""
from pydantic import BaseModel


class AgentResult(BaseModel):
    answer: str = ""
