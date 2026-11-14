from typing import List
from services.db.database_client import db
from services.db.todo_sql import TodoSQL
from models.todo import Todo


class TodoService:
    @staticmethod
    def get_todos() -> list[Todo]:
        todo_sqls = db.session.execute(db.select(TodoSQL)).scalars().all()
        return [Todo.from_sql(item) for item in todo_sqls]
    @staticmethod
    def create_todo(title: str) -> Todo:
        if not title or not title.strip():
            raise ValueError("Title is required")
        todo = Todo(title=title.strip())

        todo_sql = todo.to_sql()
        db.session.add(todo_sql)
        db.session.commit()

        return Todo.from_sql(todo_sql)