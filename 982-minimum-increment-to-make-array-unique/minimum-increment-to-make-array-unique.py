class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sort_num = sorted(nums)
        count = 0
        print(0,sort_num)
        for i in range(1,len(sort_num)):
            if sort_num[i-1] >= sort_num[i]:
                increment = sort_num[i-1] + 1 - sort_num[i]
                sort_num[i] += increment
                count += increment
        return count
