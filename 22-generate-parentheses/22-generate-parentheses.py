class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bt(dic, temp = []):
            if len(temp)==2*n:
                ans.append(temp)
                return
            for key in dic:
                if not dic[key]:
                    return
                l, r = "(", ")"
                if dic[l] >= dic[r] and dic[key]==')':
                    continue 
                if dic[l]>dic[r]:
                    continue
                dic[key]-=1
                bt(dic, temp+[key])
                dic[key]+=1
                
        bt({")":n, "(":n})
        return [''.join(i) for i in ans]
            