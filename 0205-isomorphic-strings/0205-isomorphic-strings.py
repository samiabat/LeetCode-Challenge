class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map  = {}
        rev = {}
        for i in range(len(s)):
            if s[i] in map and map[s[i]] != t[i]:
                return False
            if s[i] not in map and t[i] in rev:
                return False
            map[s[i]] = t[i]
            rev[t[i]] = s[i]
        return True