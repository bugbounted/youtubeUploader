import asyncio
from aiogram import executor

import filters
import handlers
from loader import dp

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message} from {addr}")

    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8000)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

    # Start the bot executor after setting up the TCP server
    executor.start_polling(dp)

if __name__ == '__main__':
    asyncio.run(main())
