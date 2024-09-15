
from os import getpid

from queue import Queue, Empty
from threading import Thread, Lock

from random import randrange
from time import sleep

from pathlib import Path
import json


def append_JSON_file(path, log_entry):
    with open(path, "a") as textiowrapper:
        json.dump(log_entry, textiowrapper)
        textiowrapper.write('\n')

class ThreadSafeList:
    def __init__(self):
        self.data = []
        self.lock = Lock()

    def append(self, item):
        with self.lock:
            self.data.append(item)

    def get_data(self):
        with self.lock:
            return self.data.copy()

def worker(thread_id, task_queue, result_list):
    while True:
        try:
            ## block=False - If the queue is empty, no more tasks to process, do not have a thread block/"wait". This throws the Empty exception.
            item = task_queue.get(block=False)
            ## Simulate work taking variable time to complete
            sleep(randrange(0, 2))
            temp_tuple = (int(thread_id), int(item))
            result_list.append(temp_tuple)
            task_queue.task_done()
        ## Exit the Queue when threads no longer have tasks assigned
        except Empty:
            break

def main():
    max_number_of_tasks = 30
    number_of_threads_utilized = 8
    task_queue = Queue()
    result_list = ThreadSafeList()

    ## Creating the list-like Queue of tasks: [0,1,2,...29]
    for task_id in range(max_number_of_tasks):
        task_queue.put(task_id)

    ## Start the worker threads
    threads = []
    for thread_id in range(number_of_threads_utilized):
        ## Define a thread
        thread = Thread(target=worker, args=(thread_id, task_queue, result_list))
        ## Add the thread to a list in order to manage it
        threads.append(thread)
        ## Start the thread
        thread.start()
        
    ## Wait for all threads to complete
    for thread in threads:
        thread.join()

    ## Creating log_entry
    log_entry = {"metadata": {
        "utilizedNumberOfThreads": number_of_threads_utilized,
        "maxNumberOfTasks": max_number_of_tasks
        },
        "orderedThreadIdTaskIdPairs": result_list.get_data()
        }

    ## Append JSON file with log_entry
    path = Path(r".\thread_logs.JSON")
    append_JSON_file(path, log_entry)


if __name__ == "__main__":
    print(f"process_id: {getpid()}\n")
    main()