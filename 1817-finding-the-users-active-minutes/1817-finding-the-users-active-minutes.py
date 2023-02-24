class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        cnt = defaultdict(set)
        for a, b in logs:
            cnt[a].add(b)
        arr = []
        for key in cnt:
            arr.append(len(cnt[key]))
        arr.sort()
        cnt = Counter(arr)
        ans  =[0] * k
        for key in cnt:
            ans[key-1] = cnt[key]
        return ans