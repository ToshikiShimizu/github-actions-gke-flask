import pytest
from script import app

def test_flask_simple():
    app.config['TESTING'] = True
    client = app.test_client() 
    result = client.get('/')
    assert b'Hello' in result.data