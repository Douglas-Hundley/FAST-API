# Imports for this project
from enum import auto
from turtle import st
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from .routers import user, post, auth
from .config import settings
# uses models package
models.Base.metadata.create_all(bind=engine)

# instantiates fastapi
app = FastAPI()


# while True:
        
#     try:
#         conn = psycopg2.connect(host='', database='', user='',
#                                 password=, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connection failed")
#         print("Error: ", error)
#         time.sleep(2)
      


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#              {"title": "favourite foods", "content": "I like pizza", "id": 2}]

# # finds posts
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
# # pulls index and post id
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}