class Solution:
    def reverseWords(self, s: str) -> str:
        new_st = s.strip('').split(' ')
        st = [i for i in new_st if i != ""]
        left = 0
        right = len(st)-1
        while(left<right):
            st[left],st[right] = st[right], st[left]
            left = left + 1
            right = right - 1
        return ' '.join(st)
