from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq_list = [i for i in range(int(math.sqrt(c)) + 1)]
        left = 0
        right = int(c**0.5)
        while left <= right:
            sum_of_vars = sq_list[left]**2  + sq_list[right]**2
            # left_sum = sq_list[left]**2 + sq_list[left]**2
            # right_sum = sq_list[right]**2 + sq_list[right]**2
            if sum_of_vars == c: #or left_sum == c or right_sum == c:
                return  True
            elif sum_of_vars > c:
                right -= 1
            elif sum_of_vars < c:
                left += 1
        return False
