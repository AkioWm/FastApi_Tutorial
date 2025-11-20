from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables
    yield


app = FastAPI()


text_posts = {1: {"title": "Engine Basics", "content": "The engine converts fuel into motion."},
    2: {"title": "Transmission", "content": "It transfers engine power to the wheels."},
    3: {"title": "Suspension", "content": "Suspension keeps the ride smooth and stable."},
    4: {"title": "Braking System", "content": "Disc brakes provide strong stopping power."},
    5: {"title": "Air Intake", "content": "Fresh air improves combustion efficiency."},
    6: {"title": "Exhaust System", "content": "It expels gases and reduces noise."},
    7: {"title": "Fuel Injection", "content": "Injectors precisely deliver fuel to the engine."},
    8: {"title": "Steering System", "content": "It allows the driver to control direction."},
    9: {"title": "Cooling System", "content": "Coolant prevents the engine from overheating."},
    10: {"title": "Battery", "content": "The battery powers electronics and starts the engine."}}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title,"content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
    