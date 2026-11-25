import asyncio
import time

def heavy_cpu_function():
    total = 0
    for i in range(20_000_000):
        total += i


async def async_tasks():
    for i in range(5):
        print(f" task {i}")
        await asyncio.sleep(0.3)


async def blocking_demo():
    async def run_cpu():
        # await asyncio.sleep(0.4)
        print("  CPU work starts")
        heavy_cpu_function()  # blocks everything
        print("  CPU work done")

    await asyncio.gather(async_tasks(), run_cpu())


asyncio.run(blocking_demo())