from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routes.character_routes import router as character_router
from app.routes.item_routes import router as item_router
from app.routes.skill_routers import router as skill_router
from app.routes.hexa_routers import router as hexa_router
from app.routes.union_routers import router as union_router
from app.routes.guilds_router import router as guild_router
from app.routes.user_routes import router as user_router

app = FastAPI()
app.include_router(character_router)
app.include_router(item_router)
app.include_router(skill_router)
app.include_router(hexa_router)
app.include_router(union_router)
app.include_router(guild_router)
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
