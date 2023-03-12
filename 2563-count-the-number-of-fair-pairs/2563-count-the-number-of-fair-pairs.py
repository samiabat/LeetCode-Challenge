class Solution:
    def countFairPairs(self, arr: List[int], lower: int, upper: int) -> int:
        prefix_arr = []
        arr.sort()
        ans = 0
        for cur_num in arr:
            left_bound = lower - cur_num
            right_bound = upper - cur_num
            left_loc = bisect_left(prefix_arr, left_bound)
            right_loc = bisect_right(prefix_arr, right_bound)
            ans += (right_loc - left_loc)
            prefix_arr.append(cur_num)
        return ans