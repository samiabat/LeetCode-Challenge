class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {order[i]:i for i in range(len(order))}
        def value(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if dic[w1[i]] > dic[w2[i]]:
                    return False
                elif dic[w1[i]] < dic[w2[i]]:
                    return True
            return len(w1) <= len(w2)
        for i in range(len(words)-1):
            if not value(words[i], words[i+1]):
                return False
        return True