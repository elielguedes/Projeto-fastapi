from fastapi import FastAPI 
from app.routes.auth import auth

app = FastAPI()


app.include_router(auth)