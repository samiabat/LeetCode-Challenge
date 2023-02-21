# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def readE(tokens):
            nested_int = NestedInteger()
            while tokens and tokens[0] != ']':
                nested_int.add(readT(tokens))
                if tokens[0] == ',':
                    tokens.popleft()
            return nested_int
        
        def readT(tokens):
            if tokens[0] == '[':
                tokens.popleft()
                nested_int = readE(tokens)
                tokens.popleft()
            else:
                nested_int = NestedInteger(int(tokens.popleft()))
            return nested_int
        
        tokens = deque(m[0] for m in re.finditer(r'\[|\]|\,|\-?\d+', s))
        return readT(tokens)