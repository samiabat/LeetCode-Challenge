class Solution:
    def minOperations(self, arr: List[int], x: int) -> int:
        position = {0:-1}
        cur_prefix = 0
        tot = sum(arr)
        to_be_removed = tot - x
        best_ans = float('inf')
        for i in range(len(arr)):
            cur_prefix += arr[i]
            removed = cur_prefix -  to_be_removed
            position[cur_prefix] = i
            if removed in position:
                cur_ans = position[removed] + 1 + (len(arr) - i - 1)
                best_ans = min(best_ans, cur_ans)
        if best_ans == inf:
            return -1
        return best_ans
            
            
        