class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
                return True
            num_dict[i] = 1 
        