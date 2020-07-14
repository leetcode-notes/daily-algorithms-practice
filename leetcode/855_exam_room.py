import bisect


class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.total = N

    def seat(self) -> int:
        n = self.total
        start, res, dist = -1, -1, 0

        for i in self.seats:
            if start == -1:
                if i > dist:
                    dist = i
                    res = 0
            else:
                if (i-start)//2 > dist:
                    dist = (i-start)//2
                    res = (i+start)//2
            start = i

        if start != -1:
            if n-1-start > dist:
                dist = n-1-start
                res = n-1
        else:
            res = 0

        bisect.insort(self.seats, res)
        return res

    def leave(self, p: int) -> None:
        self.seats.remove(p)


s = ExamRoom(10)
s.seat()
s.seat()
s.seat()
s.seat()

'''
Success
Details
Runtime: 260 ms, faster than 56.57% of Python3
Memory Usage: 14.1 MB, less than 62.55% of Python3
Next challenges:
Range Module
My Calendar II
Hand of Straights
'''


class ExamRoomTLE:

    def __init__(self, N: int):
        self.seats = [0 for _ in range(N)]
        self.occupied = set()

    def seat(self) -> int:
        if len(self.occupied) == 0:
            self.seats[0] = 1
            self.occupied.add(0)
            return 0
        prev, dist = None, 0
        new_seat = 0
        for i, n in enumerate(self.seats):
            if n == 1:
                if prev is None:
                    dist = i
                    if self.seats[0] == 0:
                        new_seat = 0
                else:
                    if (i-prev)//2 > dist:
                        dist = (i-prev)//2
                        new_seat = (i-dist)
                prev = i
        if len(self.seats)-1-prev > dist:
            new_seat = len(self.seats)-1
        self.seats[new_seat] = 1

        return new_seat

    def leave(self, p: int) -> None:
        self.seats[p] = 0

        # Your ExamRoom object will be instantiated and called as such:
        # obj = ExamRoom(N)
        # param_1 = obj.seat()
        # obj.leave(p)
