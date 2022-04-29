class TrieNode:
    def __init__(self, char = ""):
        self.children = {}
        self.endWith = False
class Tries:
    def __init__(self):
        self.dic = {}
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.endWith = True
        if word in self.dic:
            self.dic[word]-=1
        else:
            self.dic[word] = -1
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return node.endWith
    def startWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return True
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        t = Tries()
        for word in words:
            t.insert(word)
        pos = []
        for key in t.dic:
            tup = (t.dic[key],key)
            heappush(pos, tup)
        result =  []
        for _ in range(k):
            result.append(heappop(pos)[1])
        return result
         
        
        
        
        
        
        