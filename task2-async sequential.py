


import asyncio
from pdb import main
import time

# Use async functions
# Create an async task function
# Call tasks like this: await task() inside a loop

async def task(i):
    print(f"Task {i}: Start")
    print(f"Task {i}: Delay for 2 seconds")
    time.sleep(2)  
    print(f"Task {i}: Finish")

async def run_async_tasks():
    start_time = time.time()
    for i in range(1, 9):
        await task(i)

    end_time = time.time()
    total_time = end_time - start_time

    # print the total execution time
    print(f"Total execution time: {total_time} seconds")

asyncio.run(run_async_tasks())