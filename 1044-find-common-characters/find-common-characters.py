class Solution:
    from collections import Counter
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
        result_list = []
        for i in range(1,len(words)):
            current_count = Counter(words[i])
            for letter in common_count.keys():#['l', 'b', 'e', 'a']
                common_count[letter] = min(current_count[letter], common_count[letter]) # common_count['l'] = min (1,2)

        for letter, count in common_count.items():
            for _ in range(count):
                result_list.append(letter)
        return result_list


