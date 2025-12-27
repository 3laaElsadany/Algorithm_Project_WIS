import time
import random


def naive_wis(jobs, index=0):
    if index >= len(jobs):
        return 0

    # Case 1: Exclude current job
    exclude = naive_wis(jobs, index + 1)

    # Case 2: Include current job
    include = jobs[index][2]
    next_index = index + 1

    while next_index < len(jobs) and jobs[next_index][0] < jobs[index][1]:
        next_index += 1

    include += naive_wis(jobs, next_index)

    return max(include, exclude)


def generate_jobs(n):
    jobs = []
    for _ in range(n):
        start = random.randint(1, 100)
        finish = start + random.randint(1, 100)
        profit = random.randint(1, 100)
        jobs.append((start, finish, profit))
    return jobs


sizes = [100, 500, 1000, 5000, 100000]

for n in sizes:
    jobs = generate_jobs(n)
    jobs.sort()  

    start_time = time.time()
    naive_wis(jobs)
    end_time = time.time()

    print(f"n = {n}, Time = {end_time - start_time:.6f} seconds")
