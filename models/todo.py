from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Optional

from flask_sqlalchemy import SQLAlchemy

from services.db.todo_sql import TodoSQL

@dataclass
class Todo:
    title: str
    id: Optional[int] = None
    completed: Optional[bool] = False
    created: datetime = field(default_factory=datetime.now)
    updated: Optional[datetime] = field(default_factory=datetime.now)
    

    def to_dict(self):
        data = asdict(self)
        if isinstance(data.get('created'), datetime):
            data['created'] = data['created'].isoformat()

        if isinstance(data.get('updated'), datetime):
            data['updated'] = data['updated'].isoformat()

        return data
    def to_sql(self) -> 'TodoSQL':
        """POSTリクエストなどで受け取ったデータクラスを、SQLAlchemyのモデル(TodoSQL)に変換する"""
        return TodoSQL(
            id=self.id,
            title=self.title,
            completed=self.completed,
            created=self.created,
            updated=self.updated
        )
    @classmethod
    def from_sql(cls, todo_sql: TodoSQL) -> 'Todo':
        """GETリクエストなどでDBから取得したTodoSQLを、Pythonのデータクラス(Todo)に復元する"""
        return cls(
            id=todo_sql.id,
            title=todo_sql.title,
            completed=todo_sql.completed,
            created=todo_sql.created,
            updated=todo_sql.updated
        )
# 動作確認用
if __name__ == "__main__":
    todo = Todo(title="テスト勉強をする")
    print(todo.to_dict())
    print(todo)
    print(todo.title)