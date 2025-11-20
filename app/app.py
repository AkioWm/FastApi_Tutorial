from fastapi import FastAPI, HTTPException

app = FastAPI()


text_posts = {1:{"title":"Nissan 400z","content":"the Nissan 400z is awesome!"}, 
                 2:{"title":"Nissan 240z","content":"the Nissan 240z is a legend !"}}

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)

