class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        cur = 0
        ans = 0
        tasks.sort(key = lambda x:x[1]-x[0], reverse = True)
        for i in range(len(tasks)):
            cost, min_cost = tasks[i]
            if min_cost > cur:
                ans += (min_cost - cur)
                cur += (min_cost - cur)
            cur -= cost
        return ans
        