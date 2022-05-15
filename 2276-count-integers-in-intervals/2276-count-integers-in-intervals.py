from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cnt = 0 
        self.intervals = SortedList()

    def add(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left((left, right))
        while k < len(self.intervals) and self.intervals[k][0] <= right: 
            l, r = self.intervals.pop(k)
            self.cnt -= r - l + 1
            right = max(right, r)
        if k and left <= self.intervals[k-1][1]: 
            l, r = self.intervals.pop(k-1)
            self.cnt -= r - l + 1
            left = l
            right = max(right, r)
        self.cnt += right - left + 1
        self.intervals.add((left, right))

    def count(self) -> int:
        return self.cnt
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()