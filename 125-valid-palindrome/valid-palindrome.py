class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        if len(string) == 1:
            return True
        for char in "\"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            string = string.replace(char, '')
        string = string.replace(' ', '')
        if string == string[::-1]:
            return True
        return False
        
