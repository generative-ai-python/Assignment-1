

import threading
import asyncio

total = 0
total_lock = threading.Lock()

def cpu_work():
    global total
    for _ in range(1000):
        with total_lock:
            total += 1


async def async_job(job_id):
    print(f"Job {job_id}: asking for CPU work")
    await asyncio.to_thread(cpu_work)   # CPU work runs in a thread
    print(f"Job {job_id}: finished")


async def task8():
    await asyncio.gather(async_job(1), async_job(2), async_job(3))
    print("Final total:", total, "(expected 3000)")

asyncio.run(task8())
