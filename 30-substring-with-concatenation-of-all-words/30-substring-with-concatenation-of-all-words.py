class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        word_count = collections.Counter(words)
        sub_str_length = word_length*k
        
        
        
        ans = []
        for i in range(n-sub_str_length+1):
            word_used = 0
            remaining = word_count.copy()
            for j in range(i, i+sub_str_length, word_length):
                word = s[j: word_length+j]
                if remaining[word]>0:
                    remaining[word]-=1
                    word_used +=1
                else:
                    break
            if word_used == k:
                ans.append(i)
        return ans
                
            
                
            
                