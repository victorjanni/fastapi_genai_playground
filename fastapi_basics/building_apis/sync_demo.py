import time
from timeit import default_timer as timer

def run_task(name,seconds):
    print(f'{name} started at: {timer()}')
    time.sleep(seconds)
    print(f'{name} finished at: {timer()}')

start =timer()
run_task('task1', 2)
run_task('task2', 3)
run_task('task3', 1)
print(f'\nTotal time taken: {timer() - start:.2f} s')    