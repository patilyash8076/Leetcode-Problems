class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = {}
        arr2_dict = {}
        li = []
        li2 = []
        for i, num in enumerate(arr2):
            arr2_dict[num] = i
        for num, i in enumerate(arr1):
            if i in arr1_dict:
                arr1_dict[i].append(num)
            else:
                arr1_dict[i] = [num]
        for i in arr2_dict:
            for count in range(len(arr1_dict[i])):
                li.append(i)
        for i in arr1:
            if i not in arr2:
                li2.append(i)
        sort_list = sorted(li2)
        for i in sort_list:
            li.append(i)
        return li