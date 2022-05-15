class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = []
        for i in pattern:
            arr.append(i)
        s = s.split()
        if len(arr)!=len(s):
            return False
        dic = {}
        for i in range(len(arr)):
            key = arr[i]
            if key not in dic:
                dic[key] = s[i]
            else:
                if dic[key]!=s[i]:
                    return False
        st = set()
        for key in dic:
            if dic[key] in st:
                return False
            st.add(dic[key])
        return True
        