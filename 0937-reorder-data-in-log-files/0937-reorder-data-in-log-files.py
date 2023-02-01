class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        leterlog = []
        digi = []
        
        nums = [str(i) for i in range(10)]
        
        for phrase in logs:
            cur = phrase.split()
            if cur[1][0] not in nums:
                leterlog.append((cur[1:], phrase))
            else:
                digi.append(phrase)
        leterlog.sort()
        for i in range(len(leterlog)):
            leterlog[i] = leterlog[i][1]
        for d in digi:
            leterlog.append(d)
        return leterlog