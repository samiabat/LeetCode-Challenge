class Trie:
    def __init__(self):
        self.child = {}
        self.end = False
        
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # insert
        
        root = Trie()
        
        
        def insert(word):
            node = root
            
            for char in word:
                if char not in node.child:
                    node.child[char] = Trie()
                node = node.child[char]
            node.end = True
        @cache
        def find(idx, word, node):
            if idx >= len(word): 
                if node.end: return True
                return False
            if word[idx] not in node.child and word[idx] not in root.child:
                return False
            
            elif word[idx] not in node.child and node.end:
                return find(idx+1, word, root.child[word[idx]])
            elif word[idx] not in node.child: return False
            one = False
            if  word[idx] in root.child and node.end: one = find(idx+1, word, root.child[word[idx]])
            return ( one or find(idx+1, word, node.child[word[idx]]))
        words.sort(key=lambda x: len(x))
        ans = []
        for word in words:
            if find(0, word, root): ans.append(word)
            insert(word)
        return ans
        
                
                
                