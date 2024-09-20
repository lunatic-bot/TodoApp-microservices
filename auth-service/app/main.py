# app/main.py

from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth_routes
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI(
    title="Auth Service",
    description="Authentication microservice for Todo App",
    version="1.0.0",
)

# Add CORS middleware if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include the auth routes
app.include_router(auth_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Auth Service!"}
