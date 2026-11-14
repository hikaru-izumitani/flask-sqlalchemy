from flask import Flask
from services.db.database_client import init_db
from routes.todo_routes import todo_blueprint
# 1. Flaskアプリの初期化
app = Flask(__name__)

# 2. データベースの設定（ここではローカルの SQLite を使用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. SQLAlchemy（db）のインスタンスを作成してアプリと紐付ける
init_db(app=app)

app.register_blueprint(todo_blueprint)

if __name__ == '__main__':
    # サーバーの起動
    app.run(debug=True, port=5000)