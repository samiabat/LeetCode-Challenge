class Solution:
    def perfect_square(self, num):
        return int(math.sqrt(num))**2 == num
    
    def numSquarefulPerms(self, nums):
        def dfs(ans, path):
            if not ans:
                res.add(tuple(path))

            for i in range(len(ans)):
                if i>0 and ans[i] == ans[i-1]:
                    continue
                if path and not self.perfect_square(path[-1] + ans[i]):
                    continue

                dfs(ans[:i] + ans[i+1:], path + [ans[i]])

        res = set()
        dfs(nums, [])

        return len(res)