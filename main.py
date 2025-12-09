from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routes.character_routes import router as character_router
from app.routes.item_routes import router as item_router
from app.routes.skill_routers import router as skill_router

app = FastAPI()
app.include_router(character_router)
app.include_router(item_router)
app.include_router(skill_router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
