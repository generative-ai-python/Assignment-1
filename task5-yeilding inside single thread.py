import asyncio
import time 
async def async_tasks():
    for i in range(1, 6):
        print(f" task {i}")
        await asyncio.sleep(1)



async def cpu_task():
    print("Starting CPU-bound task...")
    total = 0
    for i in range(10000000):
        total += i
        if i % 100000 == 0:
            await asyncio.sleep(0) 
    print("CPU-bound task completed.")


async def yielding_function():
    start = time.time()
    await asyncio.gather(async_tasks(), cpu_task())
    end = time.time()
    print(f"All tasks completed in {end - start:.2f} seconds.")


asyncio.run(yielding_function())