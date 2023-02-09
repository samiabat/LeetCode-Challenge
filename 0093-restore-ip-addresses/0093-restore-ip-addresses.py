class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def bt(temp, idx):
            if len(temp) == 4 and idx>= len(s):
                ans.append(temp.copy())
                return
            elif len(temp) >= 4 or idx >= len(s):
                return
            num = ''
            while idx<len(s) and int(num + s[idx]) <= 255 and (not num or num[0] != '0'):
                num += s[idx]
                bt(temp + [num], idx+1)
                idx += 1   
        bt([], 0)
        return ['.'.join(i) for i in ans]


