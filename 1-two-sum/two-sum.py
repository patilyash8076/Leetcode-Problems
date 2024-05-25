class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict ={}
        # for index, num in enumerate(nums):
        #     if num not in my_dict:
        #         my_dict[num] = []
        #     my_dict[num].append(index)  
        for i in range(len(nums)):      # iterating over nums
            if nums[i] not in my_dict:  # checking if the number is already present or not in my_dict
                my_dict[nums[i]] = []   # if not then initiating list for that num
            my_dict[nums[i]].append(i)  # appending indexes of all num and storing them to my_dict
        print(my_dict)
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums)-1
        while left < right:
            current_sum = sorted_nums[left] + sorted_nums[right]
            if current_sum > target:
                right = right - 1
            elif current_sum < target:
                left = left + 1
            else:
                if sorted_nums[left] == sorted_nums[right]:                    
                    return [my_dict[sorted_nums[left]][0],my_dict[sorted_nums[right]][1]]
                return [my_dict[sorted_nums[left]][0],my_dict[sorted_nums[right]][0]]
