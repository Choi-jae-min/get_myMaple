from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.character_routes import router as maple_router

load_dotenv()
app = FastAPI()
app.include_router(maple_router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
