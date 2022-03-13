class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        tot=0
        for i in grid:
            l = 0
            r = len(i)-1
            if len(i)==1:
                if i[0]<0:
                    tot+=1
                    continue
            if i[l]<0:
                tot+=len(i)
                continue
            while l<=r:
                m = (l+r)//2
                if i[m]<0 and i[m-1]>=0:
                    tot=tot+len(i)-m
                    break
                elif i[m]<0:
                    r = m-1
                elif i[m]>=0 and m+1>=len(i):
                    break
                elif i[m]>=0:
                    l = m+1
        return tot
                
                    