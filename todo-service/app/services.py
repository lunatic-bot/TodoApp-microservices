# services.py
from sqlalchemy.orm import Session
from app.models.todos import TodoItem
from app.schemas.schemas import TodoCreate, TodoUpdate
from datetime import datetime

def create_todo(db: Session, todo: TodoCreate) -> TodoItem:
    """
    Create a new todo item in the database.
    """
    db_todo = TodoItem(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        user_id=todo.user_id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo_by_id(db: Session, todo_id: int) -> TodoItem:
    """
    Retrieve a todo item by its ID.
    """
    return db.query(TodoItem).filter(TodoItem.id == todo_id).first()

def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> TodoItem:
    """
    Update an existing todo item.
    """
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        if todo_update.title is not None:
            db_todo.title = todo_update.title
        if todo_update.description is not None:
            db_todo.description = todo_update.description
        if todo_update.completed is not None:
            db_todo.completed = todo_update.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> TodoItem:
    """
    Delete a todo item from the database.
    """
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo

def get_todos_for_user(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> list[TodoItem]:
    """
    Retrieve all todo items for a specific user.
    """
    return db.query(TodoItem).filter(TodoItem.user_id == user_id).offset(skip).limit(limit).all()
