class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = ""
        left = 0
        s = list(s)
        right = len(s)-1
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        while(left<right):
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left +=1
                right -=1
        return "".join(s)





                