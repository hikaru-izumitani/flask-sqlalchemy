from flask import Blueprint
from controllers.todo_controller import TodoController

todo_blueprint = Blueprint('todo', __name__, url_prefix='/todos')

@todo_blueprint.route('', methods=['GET'])
def get_todos():
    return TodoController.get_todos()

@todo_blueprint.route('', methods=['POST'])
def create_todo():
    return TodoController.create_todo()