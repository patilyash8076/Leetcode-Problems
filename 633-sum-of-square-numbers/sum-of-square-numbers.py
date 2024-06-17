# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         sq_list = [i for i in range(0,c+1)]
#         left = 0
#         right = int(c**0.5)
#         while left <= right:
#             sum_of_vars = sq_list[left]**2  + sq_list[right]**2
#             left_sum = sq_list[left]**2 + sq_list[left]**2
#             right_sum = sq_list[right]**2 + sq_list[right]**2
#             if sum_of_vars == c or left_sum == c or right_sum == c:
#                 return  True
#             elif sum_of_vars > c:
#                 right -= 1
#             elif sum_of_vars < c:
#                 left += 1
#         return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)  # Only need to consider up to the square root of c
        while left <= right:
            current_sum = left**2 + right**2
            if current_sum == c:
                return True
            elif current_sum > c:
                right -= 1
            else:
                left += 1
        return False

            
        