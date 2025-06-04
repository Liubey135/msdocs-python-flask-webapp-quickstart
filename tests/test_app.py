import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Azure' in response.data

def test_hello_with_name_and_country(client):
    response = client.post('/hello', data={'name': 'Alice', 'country': 'Wonderland'})
    assert response.status_code == 200
    assert b'Hello Alice' in response.data
    assert b'From: Wonderland' in response.data

def test_hello_redirects_without_name(client):
    response = client.post('/hello', data={'name': '', 'country': 'Nowhere'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to Azure' in response.data 