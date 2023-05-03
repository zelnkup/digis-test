from starlette.testclient import TestClient

from server import app


def test_pong_response():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("ping")
        data = websocket.receive_text()
        assert data == "pong"
