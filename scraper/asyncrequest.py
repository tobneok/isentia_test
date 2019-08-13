import aiohttp
import asyncio
import logging

"""
This class fetches (HTTP GET) pages asynchronously. This allows multiple pages
to be fetched in parallel, without using threads or processes (memory-friendly).

When the fetch is finished, the callback function cb is called.
If the callback function returns True, the page was bad and we retry the call.

To increase realism, a delay can be specified, which is the number of seconds
to wait before fetching the page.
"""

class AsyncRequest:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.tasks = []

    def get_page(self, url, cb, delay=0):
        logging.debug("Fetching %s" % url)
        headers = {
            'Accept-Language': "en-US,en;q=0.8",
            'User-Agent': "XXX"
        }
        task = asyncio.ensure_future(self._task(url, headers, cb, delay))
        self.tasks.append(task)

    def run(self):
        self.loop.run_until_complete(asyncio.gather(*self.tasks))

    async def _task(self, url, headers, cb, delay):
        await asyncio.sleep(delay)
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    html = await self._get(session, url, headers)
                retry = cb(html)
                if not retry: # If the callback gives back True, it means something went wrong during parsing, or the page is bad, and we should retry.
                    return
            except Exception as e: # Automatically retry when there is an error in fetching the page.
                logging.error(str(e))
                logging.error("Error in fetching %s, retrying soon." % url)
            await asyncio.sleep(2 * 60)

    async def _get(self, session, url, headers):
        async with session.get(url, headers=headers) as resp:
            return await resp.text()
