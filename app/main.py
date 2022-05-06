# Imports for this project
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post, auth, vote

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
app.include_router(vote.router)
@app.get("/")
def root():
    return {"message": "Hello World"}