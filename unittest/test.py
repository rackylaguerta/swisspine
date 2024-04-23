import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using Flask's built-in testing support
    with app.test_client() as client:
        yield client

def test_mirror_word_with_word(client):
    # Test with a word provided
    response = client.get('/api/mirror?word=hellO123')
    assert response.status_code == 200
    assert response.json == {"transformed": "321oLLEH"}
