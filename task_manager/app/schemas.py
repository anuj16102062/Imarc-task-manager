from pydantic import BaseModel, field_validator
from typing import Optional
from uuid import UUID
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Title must not be empty')
        if len(v.strip()) < 6:
            raise ValueError('Title must be at least 6 characters long')
        return v.strip()

    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError('Description must not be empty if provided')
        return v.strip() if v else v


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    @field_validator('title')
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError('Title must not be empty if provided')
        return v.strip() if v else v


class TaskOut(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    completed: bool

    model_config = {
        "from_attributes": True
    }
