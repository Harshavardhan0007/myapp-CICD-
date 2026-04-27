import pytest
from app import app

# This creates a test version of your app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test 1 - Does home page load?
def test_home_page_loads(client):
    result = client.get('/')
    assert result.status_code == 200

# Test 2 - Does page contain correct text?
def test_home_page_content(client):
    result = client.get('/')
    assert b'DevOps Pipeline' in result.data

# Test 3 - Does wrong page return 404?
def test_wrong_page(client):
    result = client.get('/wrongpage')
    assert result.status_code == 404
