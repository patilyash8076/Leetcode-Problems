class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict ={}
        for index, num in enumerate(nums):
            if num not in my_dict:
                my_dict[num] = []
            my_dict[num].append(index)   
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
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Building a dictionary to map values to all their indices
#         num_to_indices = {}
#         for index, num in enumerate(nums):
#             if num not in num_to_indices:
#                 num_to_indices[num] = []
#             num_to_indices[num].append(index)
#         print(num_to_indices)
#         # Sort the numbers to use two-pointer technique
#         nums.sort()
#         left, right = 0, len(nums) - 1

#         while left < right:
#             current_sum = nums[left] + nums[right]
#             if current_sum > target:
#                 right -= 1
#             elif current_sum < target:
#                 left += 1
#             else:  # current_sum == target
#                 # If elements are the same, handle accordingly
#                 if nums[left] == nums[right]:
#                     return [num_to_indices[nums[left]][0], num_to_indices[nums[right]][1]]
#                 return [num_to_indices[nums[left]][0], num_to_indices[nums[right]][0]]

#         return []  # If no two numbers sum up to the target