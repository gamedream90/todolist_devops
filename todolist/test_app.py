import pytest
# Assuming 'app' is the Flask application instance in todolist/app.py
from app import app 

# Fixture to create a testing client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Create an instance of the test client
    with app.test_client() as client:
        yield client

# Test 1: Check if the homepage loads successfully
def test_homepage_status(client):
    rv = client.get('/')
    # Assert that the HTTP status code is 200 (OK)
    assert rv.status_code == 200
    
# Test 2: Check if a key phrase is present on the page
def test_homepage_content(client):
    rv = client.get('/')
    # Assert that the expected header text is found
    assert b"Todo List" in rv.data