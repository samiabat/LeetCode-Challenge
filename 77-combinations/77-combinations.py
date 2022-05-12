class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        dic = Counter([i for i in range(1, n+1)])
        ans = []
        def bt(index, res = []):
            if len(res)==k:
                ans.append(res)
                return
            for key in range(index+1, n+1):
                if dic[key]:
                    dic[key]-=1
                    bt(key, res + [key])
                    dic[key]+=1
        bt(0)
        return ans