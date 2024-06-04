from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        even_list, odd_list = [], []
        summ = 0
        count_dict = Counter(s)
        occur_list = count_dict.values()
        occurences = sorted(occur_list, reverse = True)
        # created two different list one to store odd numbers and another to store even numbers
        for i in occurences:
            if i % 2 == 0:
                even_list.append(i)
            elif i % 2 != 0:
                odd_list.append(i)
        # check if odd_list have element more than 1 
        if len(odd_list) > 0:
            even_list.append(odd_list[0]) # then appending 0th element i.e biggest odd number to even list
            for i in range(1, len(odd_list)): # starting iteratiom from 1st element
                if odd_list[i] != 1:
                    odd_list[i] -= 1
                    even_list.append(odd_list[i])

        if len(even_list) == 1:            # if length of even list is 1 then return it 
            return even_list[0]
        else:
            for i in range(0,len(even_list)):
                summ += even_list[i]
            return summ




        