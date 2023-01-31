class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, 0
        cnt_white = 0
        ans = len(blocks)
        while right < len(blocks):
            if right >= k:
                ans = min(ans, cnt_white)
                cnt_white -= int(blocks[left] == 'W')
                left += 1
            cnt_white += int(blocks[right] == 'W')
            right += 1
        return min(ans, cnt_white)
                
                
        