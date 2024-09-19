# main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import todo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(todo_router.router, prefix="/todos", tags=["todos"])

# Define root endpoint for health check or basic info
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Service API"}
