import pytest
from app.api import app
def test_flask_simple():
    app.config['TESTING'] = True
    client = app.test_client() 
    result = client.get('/')
    assert b'Hallo' in result.data