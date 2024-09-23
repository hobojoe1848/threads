from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randrange


class ThreadingTaskManager:
    def __init__(self, max_number_of_tasks, number_of_threads):
        self.task_queue = Queue()
        self.results = []
        self.max_number_of_tasks = max_number_of_tasks
        self.number_of_threads = number_of_threads

    def queue_tasks(self):
        for task_id in range(self.max_number_of_tasks):
            self.task_queue.put(task_id)

    def worker(self, thread_id):
        while True:
            task_id= self.task_queue.get()
            print(f"Task: {task_id}, Thread_ID: {thread_id}")
            if task_id is None:
                break
            temp_tuple = (int(thread_id), int(task_id))
            self.results.append(temp_tuple)
            sleep(randrange(0,2))  # Simulate work
            self.task_queue.task_done()

    def manage_threads(self):
        with ThreadPoolExecutor(self.number_of_threads) as executor:
            # Start worker threads
            for thread_id in range(self.number_of_threads):
                executor.submit(self.worker, thread_id)
        
            # Wait for all tasks to be completed
            self.task_queue.join()
            
            # Stop workers
            for _ in range(self.number_of_threads):
                self.task_queue.put(None)

    def run(self):
        self.queue_tasks()
        self.manage_threads()
        return self.results
