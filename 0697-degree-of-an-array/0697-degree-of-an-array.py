class Solution:
    def findShortestSubArray(self, arr: List[int]) -> int:
        left = 0
        right = 0
        
        dg = max(Counter(arr).values())
        
        cnt = Counter()
        ans = inf
        
        while right<len(arr):
            cnt[arr[right]] += 1
            while left <= right and cnt[arr[right]] >= dg:
                ans = min(ans, right - left + 1)
                cnt[arr[left]] -= 1
                left += 1
            right += 1
        return ans
        