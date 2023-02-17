class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # assumption 
        # have variable open
        # open 
        # close or open

        ans = []
        def bt(char, open):
            if len(char) == 2*n and not open:
                ans.append(char)
                return
            if len(char) >= 2*n: return
            
            bt(char + '(', open + 1)
            if open: bt(char  + ')', open - 1)
        bt('', 0)
        return ans

