def job_sequencing(jobs):   
    jobs.sort(key=lambda x: x[1], reverse=True)
    n = len(jobs)
    result = [-1] * n  
    slot = [False] * n   
    for job in jobs:
        for j in range(min(n, job[2]) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job[0]
                break
    total_profit = sum([job[1] for i, job in enumerate(jobs) if result.count(job[0]) > 0])
    job_sequence = [result[i] for i in range(n) if result[i] != -1]
    return job_sequence, total_profit
jobs = [(1, 10, 2), (2, 19, 1), (3, 27, 2), (4, 25, 1), (5, 15, 3)]
sequence, profit = job_sequencing(jobs)
print("Job Sequence:", sequence)
print("Total Profit:", profit)
