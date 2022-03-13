class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        upper= []
        for ix,number in enumerate(heights):
            step = number-heights[ix-1]
            if ix>0 and number>heights[ix-1]:
                heappush(upper,step)
                if ladders>0:
                    ladders-=1
                elif bricks>= upper[0]:
                    bricks -= heappop(upper)
                else:
                    return ix-1
        return len(heights)-1