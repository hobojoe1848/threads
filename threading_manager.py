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
    def __init__(self, max_number_of_tasks, number_of_threads):
        self.max_number_of_tasks = max_number_of_tasks
        self.number_of_threads = number_of_threads
        self.task_queue = Queue()
        self.results = ThreadSafeList()

    def worker(self, thread_id):
        while True:
            try:
                task_id = self.task_queue.get(block=False)
                #print(f"Task_ID: {task_id}, Thread_ID: {thread_id}")
                sleep(randrange(0, 2))
                temp_tuple = (int(thread_id), int(task_id))
                self.results.append(temp_tuple)
                self.task_queue.task_done()
            except Empty:
                return ## Exit the thread when the queue is empty. Alternative would be to replace 'return' with 'break'

    def run_tasks(self):
        ## Add tasks to the queue
        for task_id in range(self.max_number_of_tasks):
            self.task_queue.put(task_id)

        ## Create individual threads up to value assigned to instance attribute self.number_of_threads, add them to a list and start each thread. Starting each thread initiates the processes taking place by the worker() method.
        threads = []
        for thread_id in range(self.number_of_threads):
            thread = Thread(target=self.worker, args=(thread_id,))
            threads.append(thread)
            thread.start()

        ## Block/wait for all tasks to be completed
        self.task_queue.join()
   
        ## Block/wait for all threads to finish
        for thread in threads:
            thread.join()

        return self.results.get_data()