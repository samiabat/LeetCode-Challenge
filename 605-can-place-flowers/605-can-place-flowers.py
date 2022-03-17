class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def helper(flowerbed, p, n):
            if n==0:
                return True
            elif p>=0 and p<len(flowerbed):
                l = p-1
                r = p+1
                if (l==-1 or flowerbed[l]==0) and (r==len(flowerbed) or flowerbed[r]==0) and flowerbed[p]==0:
                    return helper(flowerbed, p+2, n-1)
                else:
                    return helper(flowerbed, p+1, n)
            return False
        return helper(flowerbed, 0, n)
            
            
    
            
            