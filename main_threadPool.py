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

    task_manager = ThreadPoolTaskManager(max_number_of_tasks, number_of_threads_utilized)
    results_list = task_manager.run()

    ## Creating log_entry
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
    print(f"process_id: {getpid()}\n")
    main()