import asyncio
async def echo_server(reader, writer):
    while True:
        data = await reader.read(100)  # Max number of bytes to read
        if not data:
            break
        writer.write(data)
        await writer.drain()  # Flow control, see later
    writer.close()

async def say_baa():
    i = 0
    while True:
        await asyncio.sleep(5)
        print('...baa {0}'.format(i))
        i += 1

async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()

# boo = asyncio.ensure_future(main('127.0.0.1', 5000))
# baa = asyncio.ensure_future(say_baa())


# inside async functions running in a loop you can simple do
# boo = asyncio.create_task(async_func1)
# baa = asyncio.create_task(async_func2)

loop = asyncio.get_event_loop()
f = asyncio.run_coroutine_threadsafe(main('127.0.0.1', 5000), loop)
f2 = asyncio.run_coroutine_threadsafe(say_baa(), loop)

loop.run_forever()