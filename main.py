from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routes.character_routes import router as maple_router

app = FastAPI()
app.include_router(maple_router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
