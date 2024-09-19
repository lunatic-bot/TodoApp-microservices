# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy Base
Base = declarative_base()

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"  # Change this to your actual database URL

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Create a new SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
