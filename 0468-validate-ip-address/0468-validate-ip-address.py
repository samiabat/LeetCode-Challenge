class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        st = set([str(i) for i in range(10)])
        oth = st.copy()
        st.update(set(['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']))
        if ':' in queryIP:
            queryIP = queryIP.split(':')
            if len(queryIP) != 8: return "Neither"
            for ele in queryIP:
                if len(ele) == 0 or len(ele) > 4:
                    return "Neither"
                for char in ele:
                    if char not in st:
                        return "Neither"
            return "IPv6"
        else:
            queryIP = queryIP.split('.')
            if len(queryIP) != 4: return "Neither"
            for ele in queryIP:
                if len(ele) == 0 or len(ele) > 4: return "Neither"
                if ele[0] == '0' and len(ele)>1: return "Neither"
                for char in ele:
                    if char not in oth:return "Neither"
                if int(ele) > 255: return "Neither"
            return "IPv4"
                    