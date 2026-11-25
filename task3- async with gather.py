import asyncio
import time

async def async_task(name,delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    
async def main():
    start=time.time()
    await asyncio.gather(async_task("task1",1),async_task("task2",3),async_task("task3",2))

    print("total time ",time.time()-start)
    
    
asyncio.run(main())