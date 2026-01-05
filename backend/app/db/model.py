# Database models/schemas

from sqlmodel import SQLModel, Field
from typing import Optional

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    amount: float
    description: str