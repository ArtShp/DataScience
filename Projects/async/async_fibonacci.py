import asyncio, time

async def fibonacci(num):
    count = 0
    count += 1
    time.sleep(0.1)
    eveloop = asyncio.get_event_loop()

    if num > 1:
        task1 = asyncio.create_task(fibonacci(num-1))
        task2 = asyncio.create_task(fibonacci(num-2))
        await asyncio.gather(task1, task2)
        return task1.result() + task2.result()
    return num

asyncio.run(fibonacci(10))

