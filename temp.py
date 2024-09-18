
from queue import Queue, Empty
from threading import Thread, Lock

from random import randrange
from time import sleep


## Parameters assigned during instantiation
# max_number_of_tasks = 30
# number_of_threads_utilized = 8


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
            item = task_queue.get(block=False)
            sleep(randrange(0, 2))
            temp_tuple = (int(thread_id), int(item))
            result_list.append(temp_tuple)
            task_queue.task_done()
        except Empty:
            break


task_queue = Queue()
result_list = ThreadSafeList()


for task_id in range(max_number_of_tasks):
    task_queue.put(task_id)

threads = []
for thread_id in range(number_of_threads_utilized):
    thread = Thread(target=worker, args=(thread_id, task_queue, result_list))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

