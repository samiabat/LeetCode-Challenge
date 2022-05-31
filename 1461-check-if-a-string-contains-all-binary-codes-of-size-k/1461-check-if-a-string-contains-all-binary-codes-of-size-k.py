class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        setofBinaries = set()
        
        if k <= len(s):
            i = 0
            for end in range(k, len(s)+1): 
                setofBinaries.add(s[i:end])
                i += 1
        else:
            return False
        if (len(setofBinaries)) == 2**k:
            return True