from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # 1st approach using Dictionary
        num_dict = {}
        for i in nums:
            if i in num_dict:
                # num_dict[i] += 1
                return True
            num_dict[i] = 1 

        # 2nd approch using set
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)