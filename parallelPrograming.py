#parallel programming with multiple cpu---> run multiple python interpreters
from multiprocessing import Process, Queue
import time
import os
import random

def timeSecondGenerate():   
    random_number = random.randint(1, 20)       
    return random_number  #t=time
    

def task(name, seconds, queue):
    
    message = f'Process ID: {os.getpid()} - Task {name} started, will wait {seconds} seconds.\n'
    queue.put(message)   

    time.sleep(seconds)
    
    message = f'Process ID: {os.getpid()} - Task {name} completed\n'
    queue.put(message)

if __name__ == "__main__":
    queue = Queue()
    processes = []
    for i in range(10):        
        t=timeSecondGenerate()
        print(f"Process--->Generated random number: {timeSecondGenerate()}\n")
        
        process = Process(target=task, args=(f'Process-{i+1}', t, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    
    while not queue.empty():
        message = queue.get()        
        print(message, end='')
        
print("--------------------------------------------------------")
# parallel programming with single CPU & time slicing Due to GIL (Global Interpreter Lock) in Python
import threading
import time

def task2(name, seconds):
   
    print(f'1---->Task {name} has started, it will wait for {seconds} seconds.\n')
   
    time.sleep(seconds)
    print(f'1---->Task {name} completed\n')

threads = []
for i in range(10):
    
    t=timeSecondGenerate()
    
    thread = threading.Thread(target=task2, args=(f'Thread-{i+1}', t))
    threads.append(thread)
    thread.start()
    print(f"threading--->Generated random number: {t} \n")

for thread in threads:
    thread.join()
    
print("--------------------------------------------------------")

#parallel programming with single CPU & time slicing Due to GIL (Global Interpreter Lock) in Python
import asyncio

async def task1():
    print("Task 1 begins...")
    await asyncio.sleep(1)
    print("Task 1 completed.")
    return "Task 1 result"

async def task2():
    print("Task 2 begins...")
    await asyncio.sleep(2)
    print("Task 2 completed.")
    return "Task 2 result"

async def main():
    # Running task1 and task2 simultaneously with asyncio.gather
    results = await asyncio.gather(task1(), task2())
    print("Results:", results)

asyncio.run(main())
