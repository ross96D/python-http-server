import socket
import interfaces
from request import Request


def get_socket(host: str, port: int):
    return socket.create_server((host, port), reuse_port=True)


def accept_connections(
    server_socket: socket.socket,
    type_request: type[interfaces.Request],
    *,
    num: int,
):
    buffer_size = 1024

    is_infinity = num <= 0

    while num > 0 or is_infinity:
        if num > 0:
            num -= 1
        conn, addr = server_socket.accept()  # wait for client request
        try:
            request = type_request()
            request.parse(conn.recv(buffer_size))
        finally:
            conn.close()


def main(type_request: type[interfaces.Request], host: str, port: int):
    print(f"starting server on {host}:{port}")
    server_socket = get_socket(host, port)
    accept_connections(server_socket, type_request, num=0)


if __name__ == "__main__":
    try:
        main(Request, "localhost", 8123)
    except KeyboardInterrupt as _:
        print("\nKeyboardInterrupt")
        exit(1)
