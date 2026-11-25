import threading
import time

shared_counter = 0
lock = threading.Lock()


def add_without_lock():
    global shared_counter
    for _ in range(1000):
        temp = shared_counter      
        time.sleep(0)              
        shared_counter = temp + 1  


def add_with_lock():
    global shared_counter
    for _ in range(1000):
        with lock:                  # only one thread inside at a time
            temp = shared_counter
            time.sleep(0)
            shared_counter = temp + 1


def run_threads(target):
    threads = [threading.Thread(target=target) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def task7():
    global shared_counter

    shared_counter = 0
    run_threads(add_without_lock)
    print("Without Lock:", shared_counter, "(expected 5000)")

    shared_counter = 0
    run_threads(add_with_lock)
    print("With Lock:   ", shared_counter, "(expected 5000)")

task7()