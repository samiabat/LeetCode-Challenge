from collections import defaultdict
class MedianFinder:
    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)
    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2!=0:
            return self.arr[len(self.arr)//2]
        else:
            l = self.arr[len(self.arr)//2 -1]
            r = self.arr[len(self.arr)//2]
            return (l+r)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()