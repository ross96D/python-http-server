import request


def test_request_parse():
    """
    To parse an http request you need to follow this steps
    1. the first line contains method, the path and the protocol in that order.
    2. the second line contains the headers of the request. Each header is separated on by a new line
    3. the body of the request comes after 2 consecutives new lines

    Take into account that the new lines are a carriage return \r and a new line \n
    """

    reqstr = "GET /my_path HTTP/1.1\r\nHost: localhost:8123\r\nUser-Agent: curl/7.68.0\r\n\r\n"
    req = request.Request()
    req.parse(bytes(reqstr, "utf-8"))
    assert req.headers().get("host") == "localhost:8123"
    assert req.headers().get("User-Agent") == "curl/7.68.0"
    assert req.protocol() == "HTTP/1.1"
    assert req.path() == "/my_path"
