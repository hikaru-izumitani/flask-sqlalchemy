from flask import jsonify, request
from services.todo_service import TodoService

class TodoController:
    @staticmethod
    def get_todos():
        try:
            todos = TodoService.get_todos()
            return jsonify([todo.to_dict() for todo in todos]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    @staticmethod
    def create_todo():
        try:
            data = request.get_json()
            title = data.get('title')

            new_todo = TodoService.create_todo(title)
            return jsonify(new_todo.to_dict()), 201
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500