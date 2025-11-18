from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint
import psycopg2


app1=FastAPI()
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None


my_posts=[{"title":"P1","content":"C1","id":1},{
    "title":"P2","content":"C2","id":2}]


@app1.get("/")
def root():
    return{"msg":"helloworld"}

@app1.get("/posts")
def root():
    return {"data":my_posts}

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
        
def find_index(id):
    for i,p in enumerate(my_posts):
        if (p['id']==id):
            return i
    

"""@app1.post('/createpost')

# This is taking from postman body 
#def create_post(payload:dict=Body(...)):
#print(payload)
def create_post(new_post:Post):
    print(new_post)
    print(new_post.dict())
    return{"data":new_post}"""

@app1.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randint(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}


@app1.get("/posts/{id}")
def get_post(id:int,response:Response):
    post=find_post(id)
    if not post:
         #response.status_code=status.HTTP_404_NOT_FOUND
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
         #return {"message":f"post with {id} not found"}
    return{"post_detail":post}


@app1.delete("/posts/{id}")
def delete_post(id:int,response:Response):
    index=find_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not exits")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app1.put("/posts/{id}")

def update_post(id:int,post:Post):
    index=find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not exits")
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {'data':post_dict}
