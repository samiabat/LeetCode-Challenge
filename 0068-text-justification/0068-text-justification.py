class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        i = 0
        
        while i<len(words):
            cur = []
            space_needed = 0
            size = 0
            
            while i<len(words) and space_needed + size + len(words[i]) <= maxWidth:
                cur.append(words[i])
                size += len(words[i])
                space_needed += 1
                i += 1
                
            extra = maxWidth - size
            
            left = extra // (len(cur) - 1) if len(cur) > 1 else 0
            other = extra // (len(cur) - 1) if len(cur) > 1 else 0
            
            added = extra % (len(cur) - 1) if len(cur) > 1 else 0
            
            end = extra - len(cur) + 1
            
            temp = []
            for j in range(len(cur)):
                if i == len(words):
                    if 0<=j<len(cur)-1:
                        temp.append(cur[j]+' ')
                    else:
                        temp.append(cur[j]+' '*end)
                    continue
                    
                if len(cur) == 1:
                    temp.append(cur[j]+' '*end)
                    
                elif 0<=j<len(cur)-1:
                    if added:
                        temp.append(cur[j]+' '*(other+1))
                        added -= 1
                    else:
                        temp.append(cur[j]+' '*other)
                else:
                    temp.append(cur[j])
            ans.append(''.join(temp))
        return ans
                
                
                