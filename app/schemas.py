from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import Field
from pydantic import ConfigDict


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class UserOut(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Post(PostBase):  # Response side
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: int = Field(ge=0, le=1)
