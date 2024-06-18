class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit, then sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers
        worker.sort()

        max_profit = 0
        total_profit = 0
        job_index = 0

        for ability in worker:
            # While the worker can do the job, update the max_profit
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the best profit this worker can achieve
            total_profit += max_profit

        return total_profit


# Below Code is giving timelimit exceeded error

# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
#         max_profit = []   
#         # dif_pro_dict = dict(zip(difficulty, profit))
#         dif_pro_dict = {}
#         temp = 0
#         for d, p in zip(difficulty, profit):
#             if d in dif_pro_dict:
#                 dif_pro_dict[d] = max(dif_pro_dict[d], p)
#             else:
#                 dif_pro_dict[d] = p
#         for work in range(len(worker)):
#             if worker[work] < min(difficulty):
#                 temp += 0 
#             else:
#                 max_work = []
#                 for i in difficulty:
#                     if i <= worker[work]:
#                         max_work.append(dif_pro_dict[i])
#                 temp += max(max_work)
#         return temp

