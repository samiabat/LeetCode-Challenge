class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        for i in range(len(str(num))):
            cur = list(str(num))
            for j in range(i+1, len(str(num))):
                cur[i], cur[j] = cur[j], cur[i]
                th = ''.join(cur)
                ans = max(ans, int(th))
                cur[i], cur[j] = cur[j], cur[i]
                
        return ans