# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         sort_num = sorted(nums)
#         ptr = 0
#         count = 0
#         for i in range(len(sort_num)-1):
#             if sort_num[i] >= sort_num[i+1]:
#                 sort_num[i+1] += 1
#                 count += 1
#             else:
#                 continue
#             print(sort_num)
#         return count
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sort_num = sorted(nums)
        count = 0
        
        # Start from the second element in the sorted list
        for i in range(1, len(sort_num)):
            # If the current number is less than or equal to the previous number
            if sort_num[i] <= sort_num[i - 1]:
                # Calculate how much increment is needed to make it larger than the previous number
                increment = sort_num[i - 1] + 1 - sort_num[i]
                sort_num[i] += increment
                count += increment
        
        return count