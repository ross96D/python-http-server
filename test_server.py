from server import accept_connections, get_socket
from request import Request
import socket
import threading
import httpx

server_socket: socket.socket = socket.socket()


def setup_module(module):
    server_socket = get_socket("localhost", 8123)
    t = threading.Thread(
        target=accept_connections,
        args=(server_socket, Request),
        kwargs={"num": 1},
    )
    t.start()


def teardown_module(module):
    pass


def test_server():
    resp = httpx.get("http://localhost:8123")
    assert resp.headers.get("content-length", "0") == "0"
