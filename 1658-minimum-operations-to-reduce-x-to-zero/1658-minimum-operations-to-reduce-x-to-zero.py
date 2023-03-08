class Solution:
    def minOperations(self, arr: List[int], x: int) -> int:
        left = 0
        right = 0
        cur_sum = 0
        ans = float('inf')
        tot = sum(arr)
        to_be_removed = tot - x
        while right<len(arr):
            cur_sum += arr[right]
            while left<=right and cur_sum > to_be_removed:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == to_be_removed:
                ans = min(ans, left  + (len(arr) - right - 1))
            right += 1
        if ans == inf:
            return -1
        return ans