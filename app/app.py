from fastapi import FastAPI ,HTTPException
from app.schemas import PostCreate


app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "FastAPI Basics", "content": "Learning how to create APIs using FastAPI"},
    3: {"title": "Python Backend", "content": "Python is widely used for backend development"},
    4: {"title": "CRUD Operations", "content": "Testing create, read, update, and delete operations"},
    5: {"title": "Uvicorn Server", "content": "Running FastAPI apps with Uvicorn"},
    6: {"title": "API Testing", "content": "Testing APIs using Swagger UI and Postman"},
    7: {"title": "Image Upload", "content": "Integrating ImageKit for image uploads"},
    8: {"title": "Database Integration", "content": "Connecting FastAPI with a database"},
    9: {"title": "Authentication", "content": "Implementing JWT authentication in FastAPI"},
    10: {"title": "Deployment", "content": "Deploying FastAPI applications to production"}
}


@app.get("/posts")
def get_all_posts(limit: int ):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_all_posts(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)


# query parameters
# reuest body and post
@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post 

