"""
The with statement also has an asynchronous version, async with. 
You can use it to write context managers that depend on asynchronous code

To create an asynchronous context manager, you need to define the .__aenter__() and .__aexit__() methods.
"""

import aiohttp
import asyncio

class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()

async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com")
    )

asyncio.run(main())