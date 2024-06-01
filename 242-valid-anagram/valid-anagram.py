from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:   
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s.items() == count_t.items():
            return True
            
