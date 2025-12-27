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


# -------- Main Program --------
n = int(input("Enter the number of jobs: "))
jobs = []

print("Enter each job as: start_time finish_time profit")

for i in range(n):
    start, finish, profit = map(int, input(f"Job {i + 1}: ").split())
    jobs.append((start, finish, profit))

jobs.sort()

max_profit = naive_wis(jobs)

print("\nMaximum obtainable profit (Naive):", max_profit)
