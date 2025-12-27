import time
import random
import bisect

def Optimized_WIS(jobs):
    jobs.sort(key=lambda job: job[1])
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]
    finish_times = [job[1] for job in jobs]

    for i in range(1, n):
        start, finish, profit = jobs[i]
        profit_including = profit
        index = bisect.bisect_right(finish_times, start) - 1
        if index >= 0:
            profit_including += dp[index]
        dp[i] = max(dp[i - 1], profit_including)

    return dp[-1]


def generate_jobs(n):
    jobs = []
    for _ in range(n):
        start = random.randint(1, 1000)
        finish = start + random.randint(1, 1000)
        profit = random.randint(1, 100)
        jobs.append((start, finish, profit))
    return jobs


sizes = [100, 500, 1000, 5000, 100000]

for n in sizes:
    jobs = generate_jobs(n)

    start_time = time.time()
    Optimized_WIS(jobs)
    end_time = time.time()

    print(f"n = {n}, Time = {end_time - start_time:.6f} seconds")