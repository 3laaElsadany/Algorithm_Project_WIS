import bisect

def Optimized_WIS(jobs):
    # Sort jobs by finish time
    jobs.sort(key=lambda job: job[1])
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]
    finish_times = [job[1] for job in jobs]

    for i in range(1, n):
        start, finish, profit = jobs[i]
        profit_including = profit

        # Find the last non-conflicting job
        index = bisect.bisect_right(finish_times, start) - 1
        if index >= 0:
            profit_including += dp[index]

        # Choose the maximum profit
        dp[i] = max(dp[i - 1], profit_including)
    return dp[-1]


n = int(input("Enter the number of jobs: "))
jobs = []
print("Enter each job as: start_time finish_time profit")

for i in range(n):
    start, finish, profit = map(int, input(f"Job {i + 1}: ").split())
    jobs.append((start, finish, profit))
max_profit = Optimized_WIS(jobs)

print("\nMaximum obtainable profit:", max_profit)