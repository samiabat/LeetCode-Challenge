class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:       
        def count_non_bigger(target):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(target // i, n)
                if target // i == 0 or cnt > k: 
                    break # no need to do further count
            return cnt
        
        m, n = min(m, n), max(m, n)
        low, high = 1, m * n
        while low < high:
            mid = low + (high - low) // 2
            count = count_non_bigger(mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low