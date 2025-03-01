import asyncio
from rnet import Impersonate, Client


async def main():
    client = Client(
        impersonate=Impersonate.Firefox135,
        user_agent="rnet",
        tls_info=True,
    )
    async with await client.get("https://tls.peet.ws/api/all") as resp:
        print("Status Code: ", resp.status_code)
        print("Version: ", resp.version)
        print("Response URL: ", resp.url)
        print("Headers: ", resp.headers)
        print("Encoding: ", resp.encoding)
        print("Content-Length: ", resp.content_length)
        print("Remote Address: ", resp.remote_addr)
        print("Peer Certificate: ", resp.peer_certificate())
        print("Content: ", await resp.text())


if __name__ == "__main__":
    asyncio.run(main())
