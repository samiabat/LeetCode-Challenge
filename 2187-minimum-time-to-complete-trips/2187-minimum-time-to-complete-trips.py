class Solution:
    def tripCalc(self,arr, t):
        tot = 0
        for i in arr:
            tot += t//i
        return tot
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # for i in range()
        left = 0
        right = min(time)*totalTrips
        while left<=right:
            mid = (left+right)//2
            if self.tripCalc(time, mid)<totalTrips and self.tripCalc(time, mid+1)>=totalTrips:
                return mid+1
            elif self.tripCalc(time, mid)<totalTrips:
                left = mid+1
            elif self.tripCalc(time, mid)>totalTrips and self.tripCalc(time, mid-1)<totalTrips:
                return mid
            elif self.tripCalc(time, mid)>totalTrips:
                right = mid-1
            elif self.tripCalc(time, mid)==totalTrips and self.tripCalc(time, mid-1)<totalTrips:
                return mid
            else:
                right = mid-1
                