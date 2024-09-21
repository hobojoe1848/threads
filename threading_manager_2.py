
from queue import Queue, Empty
from threading import Thread, Lock
from random import randrange
from time import sleep

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

class ThreadingTaskManager: 
    def __init__(self, max_number_of_tasks, number_of_threads_utilized):
        self.max_number_of_tasks = max_number_of_tasks
        self.number_of_threads_utilized = number_of_threads_utilized
        self.task_queue = Queue()
        self.result_list = ThreadSafeList()

    def worker(self, thread_id):
        while True:
            try:
                item = self.task_queue.get(block=False)
                sleep(randrange(0, 2))
                temp_tuple = (int(thread_id), int(item))
                self.result_list.append(temp_tuple)
                self.task_queue.task_done()
            except Empty:
                return ############## Exit the thread when the queue is empty. Primary difference from other file being employed, return vs break

    def run_tasks(self):
        for task_id in range(self.max_number_of_tasks):
            self.task_queue.put(task_id)

        threads = []
        for thread_id in range(self.number_of_threads_utilized):
            thread = Thread(target=self.worker, args=(thread_id,))
            threads.append(thread)
            thread.start()

        self.task_queue.join()  # Wait for all tasks to be completed
   
        for thread in threads:
            thread.join() # Wait for all threads to finish

        return self.result_list.get_data()