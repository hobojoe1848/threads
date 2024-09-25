from threading_manager import ThreadingTaskManager ## custom module
from threadPool_manager import ThreadPoolTaskManager ## custom module

from os import getpid

from pathlib import Path
import json


def append_JSON_file(path, log_entry):
    with open(path, "a") as textiowrapper:
        json.dump(log_entry, textiowrapper)
        textiowrapper.write('\n')


def main():

    max_number_of_tasks = 30
    number_of_threads_utilized = 8

    print("This program simulates assigning 30 tasks to 8 threads, generates a JSON formatted log of the activity and updates a JSON file with the log.")

    while True:
        try:
            user_input = int(input("\nEnter 1 to run the task utilizing the 'threading' module,\nenter 2 to run the task utilizing the 'concurrent.futures' module or\nenter 0 to exit the program: "))

            if user_input == 0:
                print("Exiting the program without performing the specified task...\n")
                break

            elif user_input == 1:
                task_manager = ThreadingTaskManager(max_number_of_tasks, number_of_threads_utilized)
                results_list = task_manager.run_tasks()

            elif user_input == 2:
                task_manager = ThreadPoolTaskManager(max_number_of_tasks, number_of_threads_utilized)
                results_list = task_manager.run_tasks()

            else:
                print("Invalid input. You must enter either 0, 1 or 2, exiting the program...\n")
                break

        except ValueError:
            print("Invalid input type, exiting the program...\n")
            break
        
        ## Creating log_entry in JSON format
        log_entry = {"metadata": {
            "utilizedNumberOfThreads": number_of_threads_utilized,
            "maxNumberOfTasks": max_number_of_tasks
            },
            "orderedThreadIdTaskIdPairs": results_list
            }
        
        ## Append JSON file with log_entry
        path = Path(r".\thread_logs.JSON")
        append_JSON_file(path, log_entry)


if __name__ == "__main__":
    print(f"\nprocess_id: {getpid()}")
    main()