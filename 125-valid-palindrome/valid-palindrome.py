class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_lower = s.lower()
        string = str_lower
        if len(str_lower) == 1:
            return True
        for char in "\"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            string = string.replace(char, '')
        string = string.replace(' ', '')
        print(string)
        if string == string[::-1]:
            return True
        return False
        
