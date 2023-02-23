class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        
        h = ay2 * (ay2 < by2) + by2 * (ay2 >= by2) - ay1 * (ay1 > by1) - by1 * (ay1 <= by1)
        b = ax2 * (ax2 < bx2) + bx2 * (ax2 >= bx2) - ax1 * (ax1 > bx1) - bx1 * (ax1 <= bx1)
        
        return True if h > 0 and b > 0 else False