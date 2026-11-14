# python -m pytest
import pytest
from app import app
from services.db.database_client import db, init_db
from models.todo import Todo

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_create_and_get_todo(client):

    response = client.post('/todos', json={'title': 'Test Todo'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Todo'
    assert data['completed'] == False

    get_response = client.get('/todos')
    assert get_response.status_code == 200
    todos = get_response.get_json()
    assert len(todos) == 1
    assert todos[0]['title'] == 'Test Todo'