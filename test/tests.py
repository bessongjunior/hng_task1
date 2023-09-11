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

        response = client.get('url_endpoint', content_type="application/json")
        data = json.loads(response.data.decode())
        assert response.status_code == HTTPStatus.OK
        assert "The endpoint worked successfully!" # in data["message"]
