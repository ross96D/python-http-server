import socket
import interfaces
from request import Request


def send_response(conn: socket.socket, status: int, body: str):
    conn.send(
        bytes(
            f"HTTP/1.1 {status} OK\r\nContent-Type: text/plain\r\nContent-Length: {len(body)}\r\n\r\n{body}",
            "utf-8",
        )
    )


def get_socket(host: str, port: int):
    return socket.create_server((host, port), reuse_port=True)


def accept_connections(
    server_socket: socket.socket,
    type_request: type[interfaces.Request],
    *,
    num: int,  # if set to 0 or lower will accept infinite number of request, if not only that number.. adding for testing prupose
):
    # # the buffer size represent the amount of bytes to be read from the request
    # buffer_size = 1024

    is_infinity = num <= 0

    # # ! Uncomment this code to pass the test_server
    # while num > 0 or is_infinity:
    #     if num > 0:
    #         num -= 1
    #     conn, _ = server_socket.accept()  # wait for a client request
    #     try:
    #         send_response(conn, 200, "")
    #     finally:
    #         conn.close()


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
