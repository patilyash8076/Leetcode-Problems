class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr_s = 0
        ptr_t = 0
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
                ptr_t += 1
            else:
                ptr_s += 1
        return len(t) - ptr_t