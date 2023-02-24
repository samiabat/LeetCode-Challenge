class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    ans += 1
                if tickets[k] == 0:
                    break
        return ans
                