# main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user_router

# Initialize FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router.router, prefix="/users", tags=["users"])
