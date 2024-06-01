from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:   
        # count_s = Counter(s)
        # count_t = Counter(t)
        # if count_s.items() == count_t.items():
        #     return True
        s_dict = {}
        t_dict= {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1
        if s_dict == t_dict:
            return  True
        return False

            
