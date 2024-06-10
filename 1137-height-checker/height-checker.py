class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        he_ptr = 0
        ex_ptr = 0
        count = 0
        while he_ptr < len(heights) and ex_ptr < len(expected):
            if heights[he_ptr] != expected[ex_ptr]:
                count += 1
            he_ptr += 1
            ex_ptr += 1
        return count