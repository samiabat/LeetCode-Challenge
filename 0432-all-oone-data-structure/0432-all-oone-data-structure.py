class Node:
    slots = 'val', 'keys', 'prev', 'next'
    def __init__(self, val):
        self.val = val
        self.keys = set()

    def delnode(self, deltgt):
        prev, nxt = deltgt.prev, deltgt.next
        prev.next, nxt.prev = nxt, prev
        deltgt.next = deltgt.prev = None
        return prev

    def insertafter(self, prev, new ):
        nxt = prev.next
        new.prev, new.next = prev, nxt
        nxt.prev = prev.next = new
        
class AllOne:
    def __init__(self):
        head = Node(0)
        head.prev = head.next = head
        self.__hd = head
        self.__k2n = {}
    def inc(self, key):
        k2n = self.__k2n
        node = k2n.get(key, self.__hd)
        newval = node.val + 1
        if node is not self.__hd:
            node.keys.discard( key )
            if len( node.keys ) == 0:
                node = self.__hd.delnode( node )
        if node.next.val != newval:
            new = Node( newval )
            self.__hd.insertafter( node, new )
        node = node.next
        node.keys.add( key )
        k2n[ key ] = node

    def dec(self, key):
        k2n = self.__k2n
        node = k2n.get(key)
        if node is None: return 
        newval = node.val - 1
        node.keys.discard( key )
        if len( node.keys ) == 0:
            node = self.__hd.delnode( node )
        else:
            node = node.prev
        if newval == 0: 
            del k2n[key]
            return
        if node.val != newval:
            new = Node( newval )
            self.__hd.insertafter( node, new )
            node = new
        node.keys.add( key )
        k2n[key] = node

    def getMaxKey(self):
        return next(iter(self.__hd.prev.keys), '')
    def getMinKey(self):
        return next(iter(self.__hd.next.keys), '')
    
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()