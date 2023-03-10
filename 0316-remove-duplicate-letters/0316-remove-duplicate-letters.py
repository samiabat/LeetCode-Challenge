class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d= collections.Counter(list(s))
        # d={}
        #bcab
        #aaab
        
        stack=[]
        st=set()
        for i in range(len(s)):
            val=s[i]
            if val in st: 
                d[val] -= 1
                continue
            while stack and stack[-1] >= val and d[stack[-1]]:
                st.remove(stack.pop())
            d[val] -= 1
            if val not in st:
                stack.append(val)
                st.add(val) 
        return ''.join(stack)
    