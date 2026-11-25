
import asyncio
import time 
async def async_tasks():
    for i in range(1, 6):
        print(f" task {i}")
        await asyncio.sleep(1)


def heavy_cpu_function():
    total = 0
    for i in range(20_000_000):
        total += i

async def to_thread_demo():
    async def run_cpu():
        await asyncio.sleep(0.4)
        print("  CPU work starts in a thread (ticker keeps going)")
        await asyncio.to_thread(heavy_cpu_function)
        print("  CPU work done")

    await asyncio.gather(async_tasks(), run_cpu())

asyncio.run(to_thread_demo())