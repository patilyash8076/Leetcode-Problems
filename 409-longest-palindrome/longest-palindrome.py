from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        even_list = []
        odd_list = []
        summ = 0
        s_lower = s
        count_dict = Counter(s_lower)
        # print(count_dict)
        occur_list = count_dict.values()
        occurences = sorted(occur_list, reverse = True)
        for i in occurences:
            if i % 2 == 0:
                even_list.append(i)
            elif i % 2 != 0:
                odd_list.append(i)
        if len(odd_list) > 0:
            even_list.append(odd_list[0])
        print(odd_list)
        print(even_list)
        if len(odd_list) > 1:
            for i in range(1, len(odd_list)):
                if odd_list[i] != 1:
                    odd_list[i] -= 1
                    even_list.append(odd_list[i])
        if len(even_list) == 1:
            return even_list[0]
        else:
            print('even_list: ',even_list)
            for i in range(0,len(even_list)):
                # if even_list[i] % 2 == 0 or even_list[i] == 1:
                summ += even_list[i]
                # elif even_list[i] % 2 != 0:
                #     summ += even_list[i] - 1
            return summ




        