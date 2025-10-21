import asyncio

shared_counter = 0
lock = asyncio.Lock()

async def increment():
    global shared_counter
    for _ in range(100000):
        async with lock:
            shared_counter += 1

async def main():
    await asyncio.gather(increment(), increment())

asyncio.run(main())
print("Final:", shared_counter)