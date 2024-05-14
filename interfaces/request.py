from abc import ABCMeta, abstractmethod
from enum import Enum


class HttpMehtod(Enum):
    GET = 1
    HEAD = 2
    POST = 3
    PUT = 4
    PATCH = 5
    DELETE = 6
    CONNECT = 7
    OPTIONS = 8
    TRACE = 9

    @staticmethod
    def parse(method: str):
        match method.upper():
            case "GET":
                return HttpMehtod.CONNECT
            case "HEAD":
                return HttpMehtod.CONNECT
            case "PUT":
                return HttpMehtod.CONNECT
            case "PATCH":
                return HttpMehtod.CONNECT
            case "DELETE":
                return HttpMehtod.CONNECT
            case "CONNECT":
                return HttpMehtod.CONNECT
            case "OPTIONS":
                return HttpMehtod.CONNECT
            case "TRACE":
                return HttpMehtod.CONNECT
            case _:
                raise Exception("unkown method " + method)


class Headers(metaclass=ABCMeta):
    @abstractmethod
    def add(self, key: str, value: str):
        """
        adds the key, value pair to the header.
        It appends to any existing values associated with key.
        The key is case insensitive.
        """
        pass

    @abstractmethod
    def delete(self, key: str, value: str):
        """
        deletes the values associated with key.
        The key is case insensitive.
        """
        pass

    @abstractmethod
    def get(self, key: str) -> str | None:
        """
        Get gets the first value associated with the given key.
        If there are no values associated with the key, Get returns None.
        It is case insensitive.
        """
        pass

    @abstractmethod
    def set(self, key: str, value: str):
        """
        sets the header entries associated with key to the single element value.
        It replaces any existing values associated with key
        """
        pass

    @abstractmethod
    def values(self, key: str) -> list[str]:
        """
        Values returns all values associated with the given key.
        It is case insensitive.
        """
        pass


class Request(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, data: bytes):
        """Parse the request from the given byte data"""
        pass

    @abstractmethod
    def headers(self) -> Headers:
        """Returns the request headers"""
        pass

    @abstractmethod
    def body(self) -> bytes:
        """Returns the request body data"""
        pass

    @abstractmethod
    def method(self) -> HttpMehtod:
        """Returns the request method"""
        pass

    @abstractmethod
    def protocol(self) -> str:
        """Returns the request method"""
        pass

    @abstractmethod
    def path(self) -> str:
        """Returns the request path"""
        pass
