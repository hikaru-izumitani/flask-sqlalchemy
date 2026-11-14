from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }
with app.app_context():
    db.create_all()


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todos():
    data = request.get_json(silent=True) or {}
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Title is required'}), 400
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
