import interfaces


class Request(interfaces.Request):
    # python constructor
    def __init__(self) -> None:
        pass

    def parse(self, data: bytes):
        print(data)

    def headers(self) -> interfaces.Headers:
        raise Exception("unimplemented")

    def method(self) -> interfaces.HttpMehtod:
        raise Exception("unimplemented")

    def body(self) -> bytes:
        raise Exception("unimplemented")

    def protocol(self) -> str:
        raise Exception("unimplemented")


def main():
    req = Request()
    req.parse(data=bytes([1, 2, 3]))


if __name__ == "__main__":
    main()
