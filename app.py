from aiohttp import web
from aiogram import executor
import asyncio

import filters
import handlers
from loader import dp

async def index(request):
    return web.Response(text="Hello, World! This is your index page.")

async def start_webapp():
    app = web.Application()
    app.router.add_get('/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    await site.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_webapp())
    loop.create_task(executor.start_polling(dp))
    loop.run_forever()
