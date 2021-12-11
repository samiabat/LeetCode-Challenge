class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 0
        s = s.strip()
        b = []
        for i in range(len(s)):
            
            if s[i] == ".":
                break
            try:
                b.append(int(s[i]))
                
            except:
                if (s[0] == "-" or s[0] == "+") and sign<1:
                    sign += 1
                    pass
                else:
                    break
        c = "" 
        if len(s)>0 and s[0] == "-":
            c+="-"
        for i in b:
            c +=str(i)
        if len(c) == 1 and c[0] == "-":
            c = ""
        if len(c)>0 and c[0]:
            c = int(c)
        else:
            return 0
        if c == 0:
            return 0
        
        elif c>(2**31)-1:
            return (2**31)-1
        elif c<(-2**31):
            return -2**31
        else:
            return str(c)