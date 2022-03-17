class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = [False]*len(arr)
        new = []
        def helper(arr, start):
            if start>=0 and start<len(arr) and not visit[start]:
                if arr[start]==0:
                    new.extend([True])
                visit[start] = True
                helper(arr, start+arr[start])
                helper(arr, start-arr[start])
        helper(arr, start)
        if new:
            return True
        return False
            