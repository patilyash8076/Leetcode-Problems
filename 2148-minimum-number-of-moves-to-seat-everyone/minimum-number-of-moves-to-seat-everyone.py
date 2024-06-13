class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted = sorted(seats)
        stu_sorted = sorted(students)
        temp = 0
        for i in range(len(seats)):
            temp += abs(stu_sorted[i] - seats_sorted[i])
        return temp


        