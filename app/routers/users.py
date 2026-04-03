from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=200)
    email: str


@router.get("", response_model=list[User])
def list_users() -> list[User]:
    return [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com"),
    ]
