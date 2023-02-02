class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path = path.split('/')
        ans.append('/')
        for ele in path:
            if ele == '..' and len(ans)>=2:
                ans.pop()
                ans.pop()
            elif ele == '..': continue
            elif ele == '.' or not ele: continue
            else:
                ans.append(ele)
                ans.append('/')
        if len(ans) >1 and ans[-1] == '/': ans.pop()
        print(path)
        return ''.join(ans)