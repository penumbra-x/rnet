# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

import builtins
import typing

class Client:
    r"""
    A client for making HTTP requests.
    """
    user_agent: typing.Optional[builtins.str]
    headers: HeaderMap
    def __new__(cls,**kwds): ...
    def get_cookies(self, url:builtins.str) -> builtins.list[builtins.str]:
        r"""
        Returns the cookies for the given URL.
        
        # Arguments
        
        * `url` - The URL to get the cookies for.
        
        # Returns
        
        A list of cookie strings.
        
        # Examples
        
        ```python
        import rnet
        
        client = rnet.Client()
        cookies = client.get_cookies("https://example.com")
        print(cookies)
        ```
        """
        ...

    def set_cookies(self, url:builtins.str, value:typing.Sequence[builtins.str]) -> None:
        r"""
        Sets cookies for the given URL.
        
        # Arguments
        
        * `url` - The URL to set the cookies for.
        * `value` - A list of cookie strings to set.
        
        # Returns
        
        A `PyResult` indicating success or failure.
        
        # Examples
        
        ```python
        import rnet
        
        client = rnet.Client()
        client.set_cookies("https://example.com", ["cookie1=value1", "cookie2=value2"])
        ```
        """
        ...

    def update(self, **kwds) -> None:
        r"""
        Updates the client with the given parameters.
        
        # Arguments
        * `params` - The parameters to update the client with.
        
        # Examples
        
        ```python
        import rnet
        
        client = rnet.Client()
        client.update(
           impersonate=rnet.Impersonate.Firefox135,
           headers={"X-My-Header": "value"},
           proxies=[rnet.Proxy.all("http://proxy.example.com:8080")],
        )
        ```
        """
        ...

    def get(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a GET request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.get("https://httpbin.org/get")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def post(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a POST request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.post("https://httpbin.org/post", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def put(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a PUT request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.put("https://httpbin.org/put", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def patch(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a PATCH request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.patch("https://httpbin.org/patch", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def delete(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a DELETE request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.delete("https://httpbin.org/delete")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def head(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a HEAD request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.head("https://httpbin.org/head")
            print(response.status_code)
        
        asyncio.run(main())
        ```
        """
        ...

    def options(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends an OPTIONS request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.options("https://httpbin.org/options")
            print(response.headers)
        
        asyncio.run(main())
        ```
        """
        ...

    def trace(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a TRACE request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.trace("https://httpbin.org/trace")
            print(response.headers)
        
        asyncio.run(main())
        ```
        """
        ...

    def request(self, method:Method, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a request with the given method and URL.
        
        # Arguments
        
        * `method` - The HTTP method to use.
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        from rnet import Method
        
        async def main():
            client = rnet.Client()
            response = await client.request(Method.GET, "https://httpbin.org/get")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def websocket(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a WebSocket request.
        
        # Arguments
        
        * `url` - The URL to send the WebSocket request to.
        * `**kwds` - Additional WebSocket request parameters.
        
        # Returns
        
        A `WebSocket` object representing the WebSocket connection.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            ws = await client.websocket("wss://echo.websocket.org")
            await ws.send(rnet.Message.from_text("Hello, WebSocket!"))
            message = await ws.recv()
            print("Received:", message.data)
            await ws.close()
        
        asyncio.run(main())
        ```
        """
        ...


class ClientParams:
    r"""
    The parameters for a request.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, Version
    
    params = rnet.RequestParams(
        impersonate=Impersonate.Chrome100,
        default_headers={"Content-Type": "application/json"},
        user_agent="Mozilla/5.0",
        timeout=10,
        connect_timeout=5,
        read_timeout=15,
        no_keepalive=True,
        no_proxy=False,
        http1_only=False,
        http2_only=True,
        referer=True
    )
    
    response = await rnet.get("https://www.rust-lang.org", **params)
    body = await response.text()
    print(body)
    ```
    """
    impersonate: typing.Optional[Impersonate]
    impersonate_os: typing.Optional[ImpersonateOS]
    impersonate_skip_http2: typing.Optional[builtins.bool]
    impersonate_skip_headers: typing.Optional[builtins.bool]
    base_url: typing.Optional[builtins.str]
    user_agent: typing.Optional[builtins.str]
    headers_order: typing.Optional[builtins.list[builtins.str]]
    referer: typing.Optional[builtins.bool]
    cookie_store: typing.Optional[builtins.bool]
    async_dns: typing.Optional[builtins.bool]
    timeout: typing.Optional[builtins.int]
    connect_timeout: typing.Optional[builtins.int]
    read_timeout: typing.Optional[builtins.int]
    no_keepalive: typing.Optional[builtins.bool]
    tcp_keepalive: typing.Optional[builtins.int]
    pool_idle_timeout: typing.Optional[builtins.int]
    pool_max_idle_per_host: typing.Optional[builtins.int]
    http1_only: typing.Optional[builtins.bool]
    http2_only: typing.Optional[builtins.bool]
    https_only: typing.Optional[builtins.bool]
    tcp_nodelay: typing.Optional[builtins.bool]
    danger_accept_invalid_certs: typing.Optional[builtins.bool]
    http2_max_retry_count: typing.Optional[builtins.int]
    tls_info: typing.Optional[builtins.bool]
    no_proxy: typing.Optional[builtins.bool]
    proxies: typing.Optional[builtins.list[Proxy]]
    interface: typing.Optional[builtins.str]
    gzip: typing.Optional[builtins.bool]
    brotli: typing.Optional[builtins.bool]
    deflate: typing.Optional[builtins.bool]
    zstd: typing.Optional[builtins.bool]

class HeaderMap:
    r"""
    A HTTP header map.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Method
    
    async def main():
        resp = await rnet.request(Method.GET, "https://www.google.com/")
        print("Headers: ", resp.headers.to_dict())
    
    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
    ```
    """
    def to_dict(self) -> dict:
        r"""
        Converts the header map to a Python dictionary.
        
        # Returns
        
        A Python dictionary representing the headers.
        """
        ...

    def __getitem__(self, key:builtins.str) -> typing.Optional[typing.Any]:
        r"""
        Gets the value of the specified header.
        
        # Arguments
        
        * `key` - The name of the header.
        
        # Returns
        
        An optional byte slice representing the value of the header.
        """
        ...

    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the header map.
        """
        ...


class Impersonate:
    r"""
    A impersonate.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...


class ImpersonateOS:
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...


class Message:
    r"""
    A WebSocket message.
    """
    text: typing.Optional[builtins.str]
    close: typing.Optional[tuple[builtins.int, typing.Optional[builtins.str]]]
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the message.
        
        # Returns
        
        A string representing the message.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the message.
        
        # Returns
        
        A string representing the message.
        """
        ...

    @staticmethod
    def from_text(text:builtins.str) -> Message:
        r"""
        Creates a new text message.
        
        # Arguments
        
        * `text` - The text content of the message.
        
        # Returns
        
        A new `Message` instance containing the text message.
        """
        ...

    @staticmethod
    def from_binary(data:typing.Sequence[builtins.int]) -> Message:
        r"""
        Creates a new binary message.
        
        # Arguments
        
        * `data` - The binary data of the message.
        
        # Returns
        
        A new `Message` instance containing the binary message.
        """
        ...

    @staticmethod
    def from_ping(data:typing.Sequence[builtins.int]) -> Message:
        r"""
        Creates a new ping message.
        
        # Arguments
        
        * `data` - The ping data of the message.
        
        # Returns
        
        A new `Message` instance containing the ping message.
        """
        ...

    @staticmethod
    def from_pong(data:typing.Sequence[builtins.int]) -> Message:
        r"""
        Creates a new pong message.
        
        # Arguments
        
        * `data` - The pong data of the message.
        
        # Returns
        
        A new `Message` instance containing the pong message.
        """
        ...

    @staticmethod
    def from_close(code:builtins.int, reason:typing.Optional[builtins.str]=None) -> Message:
        r"""
        Creates a new close message.
        
        # Arguments
        
        * `code` - The close code.
        * `reason` - An optional reason for closing.
        
        # Returns
        
        A new `Message` instance containing the close message.
        """
        ...


class Method:
    r"""
    A HTTP method.
    """
    ...

class Proxy:
    r"""
    A proxy server for a request.
    """
    @staticmethod
    def http(url:builtins.str, username:typing.Optional[builtins.str]=None, password:typing.Optional[builtins.str]=None, custom_http_auth:typing.Optional[builtins.str]=None, exclusion:typing.Optional[builtins.str]=None) -> Proxy:
        r"""
        Creates a new HTTP proxy.
        
        This method sets up a proxy server for HTTP requests.
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        * `username` - Optional username for proxy authentication.
        * `password` - Optional password for proxy authentication.
        * `custom_http_auth` - Optional custom HTTP authentication header value.
        * `exclusion` - Optional list of domains to exclude from proxying.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.http("http://proxy.example.com")
        ```
        """
        ...

    @staticmethod
    def https(url:builtins.str, username:typing.Optional[builtins.str]=None, password:typing.Optional[builtins.str]=None, custom_http_auth:typing.Optional[builtins.str]=None, exclusion:typing.Optional[builtins.str]=None) -> Proxy:
        r"""
        Creates a new HTTPS proxy.
        
        This method sets up a proxy server for HTTPS requests.
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        * `username` - Optional username for proxy authentication.
        * `password` - Optional password for proxy authentication.
        * `custom_http_auth` - Optional custom HTTP authentication header value.
        * `exclusion` - Optional list of domains to exclude from proxying.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.https("https://proxy.example.com")
        ```
        """
        ...

    @staticmethod
    def all(url:builtins.str, username:typing.Optional[builtins.str]=None, password:typing.Optional[builtins.str]=None, custom_http_auth:typing.Optional[builtins.str]=None, exclusion:typing.Optional[builtins.str]=None) -> Proxy:
        r"""
        Creates a new proxy for all protocols.
        
        This method sets up a proxy server for all types of requests (HTTP, HTTPS, etc.).
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        * `username` - Optional username for proxy authentication.
        * `password` - Optional password for proxy authentication.
        * `custom_http_auth` - Optional custom HTTP authentication header value.
        * `exclusion` - Optional list of domains to exclude from proxying.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.all("https://proxy.example.com")
        ```
        """
        ...


class RequestParams:
    r"""
    The parameters for a request.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, Version
    
    params = rnet.RequestParams(
        impersonate=Impersonate.Chrome100,
        version=Version.HTTP_2,
        user_agent="Mozilla/5.0",
        headers={"Content-Type": "application/json"},
        timeout=10,
        connect_timeout=5,
        read_timeout=15,
        no_keepalive=True,
        no_proxy=False,
        http1_only=False,
        http2_only=True,
        referer=True
    )
    
    response = await rnet.get("https://www.rust-lang.org", **params)
    body = await response.text()
    print(body)
    ```
    """
    proxy: typing.Optional[builtins.str]
    interface: typing.Optional[builtins.str]
    timeout: typing.Optional[builtins.int]
    read_timeout: typing.Optional[builtins.int]
    version: typing.Optional[Version]
    auth: typing.Optional[builtins.str]
    bearer_auth: typing.Optional[builtins.str]
    basic_auth: typing.Optional[tuple[builtins.str, typing.Optional[builtins.str]]]
    query: typing.Optional[builtins.list[tuple[builtins.str, builtins.str]]]
    form: typing.Optional[builtins.list[tuple[builtins.str, builtins.str]]]
    body: typing.Optional[builtins.list[builtins.int]]

class Response:
    r"""
    A response from a request.
    
    # Examples
    
    ```python
    import asyncio
    import rnet
    
    async def main():
        response = await rnet.get("https://www.rust-lang.org")
        print("Status Code: ", response.status_code)
        print("Version: ", response.version)
        print("Response URL: ", response.url)
        print("Headers: ", response.headers.to_dict())
        print("Content-Length: ", response.content_length)
        print("Encoding: ", response.encoding)
        print("Remote Address: ", response.remote_addr)
    
        text_content = await response.text()
        print("Text: ", text_content)
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """
    url: builtins.str
    ok: builtins.bool
    status: builtins.int
    status_code: StatusCode
    version: Version
    headers: HeaderMap
    content_length: builtins.int
    remote_addr: typing.Optional[SocketAddr]
    encoding: builtins.str
    def peer_certificate(self) -> typing.Optional[builtins.list[builtins.int]]:
        r"""
        Returns the TLS peer certificate of the response.
        
        # Returns
        
        A Python object representing the TLS peer certificate of the response.
        """
        ...

    def text(self) -> typing.Any:
        r"""
        Returns the text content of the response.
        
        # Returns
        
        A Python object representing the text content of the response.
        """
        ...

    def text_with_charset(self, encoding:builtins.str) -> typing.Any:
        r"""
        Returns the text content of the response with a specific charset.
        
        # Arguments
        
        * `default_encoding` - The default encoding to use if the charset is not specified.
        
        # Returns
        
        A Python object representing the text content of the response.
        """
        ...

    def json(self) -> typing.Any:
        r"""
        Returns the JSON content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def json_str(self) -> typing.Any:
        r"""
        Returns the JSON string content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def json_str_pretty(self) -> typing.Any:
        r"""
        Returns the JSON pretty string content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def bytes(self) -> typing.Any:
        r"""
        Returns the bytes content of the response.
        
        # Returns
        
        A Python object representing the bytes content of the response.
        """
        ...

    def stream(self) -> Streamer:
        r"""
        Returns the stream content of the response.
        
        # Returns
        
        A Python object representing the stream content of the response.
        """
        ...

    def close(self) -> None:
        r"""
        Closes the response connection.
        """
        ...


class SocketAddr:
    r"""
    A IP socket address.
    """
    def ip(self) -> typing.Any:
        r"""
        Returns the IP address of the socket address.
        """
        ...

    def port(self) -> builtins.int:
        r"""
        Returns the port number of the socket address.
        """
        ...

    def __str__(self) -> builtins.str:
        r"""
        Returns the socket address as a string.
        """
        ...


class StatusCode:
    r"""
    HTTP status code.
    """
    def as_int(self) -> builtins.int:
        r"""
        Return the status code as an integer.
        """
        ...

    def is_informational(self) -> builtins.bool:
        r"""
        Check if status is within 100-199.
        """
        ...

    def is_success(self) -> builtins.bool:
        r"""
        Check if status is within 200-299.
        """
        ...

    def is_redirection(self) -> builtins.bool:
        r"""
        Check if status is within 300-399.
        """
        ...

    def is_client_error(self) -> builtins.bool:
        r"""
        Check if status is within 400-499.
        """
        ...

    def is_server_error(self) -> builtins.bool:
        r"""
        Check if status is within 500-599.
        """
        ...

    def __str__(self) -> builtins.str:
        r"""
        Returns a str representation of the `StatusCode`
        """
        ...

    def __repr__(self) -> builtins.str:
        ...


class Streamer:
    r"""
    A streaming response.
    This is an asynchronous iterator that yields chunks of data from the response stream.
    This is used to stream the response content.
    This is used in the `stream` method of the `Response` class.
    This is used in an asynchronous for loop in Python.
    
    # Examples
    
    ```python
    import asyncio
    import rnet
    from rnet import Method, Impersonate
    
    async def main():
        resp = await rnet.get("https://httpbin.org/stream/20")
        print("Status Code: ", resp.status_code)
        print("Version: ", resp.version)
        print("Response URL: ", resp.url)
        print("Headers: ", resp.headers.to_dict())
        print("Content-Length: ", resp.content_length)
        print("Encoding: ", resp.encoding)
        print("Remote Address: ", resp.remote_addr)
    
        streamer = resp.stream()
        async for chunk in streamer:
            print("Chunk: ", chunk)
            await asyncio.sleep(0.1)
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """
    def __aiter__(self) -> Streamer:
        r"""
        Returns the `Streamer` instance itself to be used as an asynchronous iterator.
        
        This method allows the `Streamer` to be used in an asynchronous for loop in Python.
        
        # Returns
        
        The `Streamer` instance itself.
        """
        ...

    def __anext__(self) -> typing.Optional[typing.Any]:
        r"""
        Returns the next chunk of the response as an asynchronous iterator.
        
        This method implements the `__anext__` method for the `Streamer` class, allowing it to be
        used as an asynchronous iterator in Python. It returns the next chunk of the response or
        raises `PyStopAsyncIteration` if the iterator is exhausted.
        
        # Returns
        
        A `PyResult` containing an `Option<PyObject>`. If there is a next chunk, it returns `Some(PyObject)`.
        If the iterator is exhausted, it raises `PyStopAsyncIteration`.
        """
        ...


class UpdateClientParams:
    r"""
    The parameters for updating a client.
    
    This struct allows you to update various settings for an existing client instance.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, UpdateClientParams
    
    params = UpdateClientParams(
        impersonate=Impersonate.Chrome100,
        headers={"Content-Type": "application/json"},
        proxies=[rnet.Proxy.all("http://proxy.example.com:8080")]
    )
    
    client = rnet.Client()
    client.update(**params)
    ```
    
    This will update the client with the specified impersonation settings, headers, and proxies.
    """
    impersonate: typing.Optional[Impersonate]
    impersonate_os: typing.Optional[ImpersonateOS]
    impersonate_skip_http2: typing.Optional[builtins.bool]
    impersonate_skip_headers: typing.Optional[builtins.bool]
    headers_order: typing.Optional[builtins.list[builtins.str]]
    proxies: typing.Optional[builtins.list[Proxy]]
    interface: typing.Optional[builtins.str]

class Version:
    r"""
    A HTTP version.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the version.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the version.
        """
        ...


class WebSocket:
    r"""
    A WebSocket response.
    """
    ok: builtins.bool
    status: builtins.int
    version: Version
    headers: HeaderMap
    remote_addr: typing.Optional[SocketAddr]
    def protocol(self) -> typing.Optional[builtins.str]:
        r"""
        Returns the WebSocket protocol.
        
        # Returns
        
        An optional string representing the WebSocket protocol.
        """
        ...

    def recv(self) -> typing.Any:
        r"""
        Receives a message from the WebSocket.
        
        # Arguments
        
        * `py` - The Python runtime.
        
        # Returns
        
        A `PyResult` containing a `Bound` object with the received message, or `None` if no message is received.
        """
        ...

    def send(self, message:Message) -> typing.Any:
        r"""
        Sends a message to the WebSocket.
        
        # Arguments
        
        * `py` - The Python runtime.
        * `message` - The message to send.
        
        # Returns
        
        A `PyResult` containing a `Bound` object.
        """
        ...

    def close(self, code:typing.Optional[builtins.int]=None, reason:typing.Optional[builtins.str]=None) -> typing.Any:
        r"""
        Closes the WebSocket connection.
        
        # Arguments
        
        * `py` - The Python runtime.
        * `code` - An optional close code.
        * `reason` - An optional reason for closing.
        
        # Returns
        
        A `PyResult` containing a `Bound` object.
        """
        ...


class WebSocketParams:
    r"""
    The parameters for a WebSocket request.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, Version
    
    params = rnet.WebSocketParams(
        proxy="http://proxy.example.com",
        local_address="192.168.1.1",
        interface="eth0",
        headers={"Content-Type": "application/json"},
        auth="Basic dXNlcjpwYXNzd29yZA==",
        bearer_auth="Bearer token",
        basic_auth=("user", "password"),
        query=[("key1", "value1"), ("key2", "value2")]
    )
    
    async with rnet.websocket("wss://echo.websocket.org") as ws:
       await ws.send("Hello, World!")
       message = await ws.recv()
       print(message)
    
    asyncio.run(run())
    ```
    """
    proxy: typing.Optional[builtins.str]
    interface: typing.Optional[builtins.str]
    auth: typing.Optional[builtins.str]
    bearer_auth: typing.Optional[builtins.str]
    basic_auth: typing.Optional[tuple[builtins.str, typing.Optional[builtins.str]]]
    query: typing.Optional[builtins.list[tuple[builtins.str, builtins.str]]]

def delete(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `DELETE` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.delete("https://httpbin.org/anything")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def get(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `GET` request.
    
    See also the methods on the [`rquest::Response`](./struct.Response.html)
    type.
    
    **NOTE**: This function creates a new internal `Client` on each call,
    and so should not be used if making many requests. Create a
    [`Client`](./struct.Client.html) instead.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.get("https://httpbin.org/anything")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    
    # Errors
    
    This function fails if:
    
    - native TLS backend cannot be initialized
    - supplied `Url` cannot be parsed
    - there was an error while sending request
    - redirect limit was exhausted
    """
    ...

def head(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `HEAD` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.head("https://httpbin.org/anything")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

def options(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make an `OPTIONS` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.options("https://httpbin.org/anything")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

def patch(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `PATCH` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.patch("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def post(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `POST` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.post("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def put(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `PUT` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.put("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def request(method:Method, url:builtins.str, **kwds) -> typing.Any:
    r"""
    Make a request with the given parameters.
    
    This function allows you to make a request with the specified parameters encapsulated in a `Request` object.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    from rnet import Method
    
    async def run():
        response = await rnet.request(Method.GET, "https://www.rust-lang.org")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def trace(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `TRACE` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.trace("https://www.rust-lang.org")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

def websocket(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Make a WebSocket connection with the given parameters.
    
    This function allows you to make a WebSocket connection with the specified parameters encapsulated in a `WebSocket` object.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
       async with rnet.websocket("wss://echo.websocket.org") as ws:
          await ws.send("Hello, World!")
         message = await ws.recv()
        print(message)
    
    asyncio.run(run())
    ```
    """
    ...

