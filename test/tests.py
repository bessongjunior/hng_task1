import pytest
import json
from http import HTTPStatus

# from ..api import app
from ..api import asgi_app as app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

    def test_endpoint(client):
        '''Test endpoint and get response.'''

        pass