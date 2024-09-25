# threads
This program is a demonstration of using Python's threading.Thread() and concurrent.futures.ThreadPoolExecutor(). It merely allows a user to choose which module.Class() to utilize to create and manage 8 threads with 30 extremely simple tasks spread across those threads, i.e. assigning a task_id of 0 through 29 to each thread with an associated delay of 0 to 2 seconds per assignment. 

User interface:

> Enter 1 to run the task utilizing the 'threading' module,
> enter 2 to run the task utilizing the 'concurrent.futures' module or
> enter 0 to exit the program:

The results track the threads generated in order via a thread_id with the associated assigned task_id in order, then it summarizes the activitity in a JSON formatted object. Lastly it appends JSON formatted information to a JSON file to create a log.

Example of results per run:

> {'metadata': {'class_utilized': 'threading.Thread', 'utilizedNumberOfThreads': 8, 'maxNumberOfTasks': 30}, 'orderedThreadIdTaskIdPairs': [(0, 0), (0, 1), (1, 3), (1, 4), (1, 5), (2, 7), (3, 9), (3, 10), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (5, 19), (5, 20), (5, 21), (6, 23), (6, 24), (7, 26), (7, 27), (7, 28), (7, 29), (0, 2), (5, 22), (4, 18), (3, 11), (2, 8), (1, 6), (6, 25)]}

