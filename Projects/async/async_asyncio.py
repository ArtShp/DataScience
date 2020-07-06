import asyncio
import time

async def tellAfter(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(tellAfter(1, 'hello'))
    task2 = asyncio.create_task(tellAfter(3, 'Andrew'))

    print(f'Начала работать в {time.strftime("%X")}')

    await task1
    await task2

    print(f'Закончила работать в {time.strftime("%X")}')


asyncio.run(main())
