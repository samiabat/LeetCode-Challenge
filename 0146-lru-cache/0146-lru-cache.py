class LRUCache:

    def __init__(self, capacity: int):
        self.memo = {}
        self.capacity = capacity
        self.order = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.memo:
            del(self.order[key])
            self.order[key] = 0
            return self.memo[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            self.memo[key] = value
            del(self.order[key])
            self.order[key] = 0
        elif len(self.order)<self.capacity:
            self.memo[key] = value
            self.order[key]=0
        else:
            top = next(iter(self.order))
            del(self.order[top])
            del(self.memo[top])
            self.memo[key] = value
            self.order[key] = 0


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)