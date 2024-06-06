from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count_dict = Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        min_heap = list(count_dict.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in count_dict: 
                    return False
                count_dict[i] -= 1
                if count_dict[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True



