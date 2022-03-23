class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        
        area = 0
        while p1<p2:
            if height[p1]>height[p2]:
                newArea = height[p2]*(p2-p1)
                p2-=1
                if newArea>area:
                    area = newArea
            else:
                newArea = height[p1]*(p2-p1)
                p1+=1
                if newArea>area:
                    area = newArea
        return area