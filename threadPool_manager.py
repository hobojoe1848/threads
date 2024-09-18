from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock
from time import sleep
from random import randrange

def printer():
    return "Cat"

class ThreadManager:
    def __init__(self, max_number_of_tasks, number_of_threads):
        self.task_queue = Queue()
        self.results = []
        self.max_number_of_tasks = max_number_of_tasks
        self.number_of_threads = number_of_threads

    def queue_tasks(self):
        for task_id in range(self.max_number_of_tasks):
            self.task_queue.put(task_id)

    def worker(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                break
            self.results.append(task)
            sleep(randrange(0,2))  # Simulate work
            self.task_queue.task_done()

    def manage_threads(self):
        with ThreadPoolExecutor(max_workers=self.number_of_threads) as executor:
            # Start worker threads
            for _ in range(self.number_of_threads):
                executor.submit(self.worker)
        
        # Wait for all tasks to be completed
        self.task_queue.join()
        
        # Stop workers
        for _ in range(self.number_of_threads):
            self.task_queue.put(None)

    def run(self):
        self.queue_tasks()
        self.manage_threads()
        return self.results