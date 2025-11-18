from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic import Field


class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


class UserOut(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime

class Post(PostBase): #Response side sending data
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        orm_mode:True  # tells pydantic model to read data even if it is not dict 

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True 

class UserCreate(BaseModel):
    email:EmailStr
    password:str


    class Config:
        orm_mode:True  # tells pydantic model to read data even if it is not dict

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int]=None

class Vote(BaseModel):
    post_id: int
    dir: int = Field(ge=0,le=1)



