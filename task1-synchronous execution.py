
import time

def run_sync_tasks():
    # Execute 8 tasks using: time.sleep()
# Each task must print: Start → delay → Finish
# Calculate the total execution time

    start_time = time.time()

    def task(i):
        print(f"Task {i}: Start")
        print(f"Task {i}: Delay for 2 seconds")
        time.sleep(2)  
        print(f"Task {i}: Finish")
    
    for i in range(1, 9):
       task(i)
        

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total execution time: {total_time} seconds")

run_sync_tasks()