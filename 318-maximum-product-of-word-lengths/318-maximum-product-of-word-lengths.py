import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = []
        for i, j in itertools.combinations(words, 2):
            com_str = ''.join(set(i).intersection(j)) 
            if len(com_str) == 0:    
                l.append(len(i)*len(j))
        if len(l) != 0:   
            return max(l)
        return 0