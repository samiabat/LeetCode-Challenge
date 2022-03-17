from typing import List
from collections import defaultdict, Counter
from itertools import chain


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        start, end = 0, n-1

        reached, frontier, matches = set(), {start}, defaultdict(list)
        for i, num in enumerate(arr):
            matches[num].append(i)

        def next_states(i):
            yield from (j for j in chain([i-1, i+1], matches[arr[i]]) if i != j and 0 <= j < n)
            matches[arr[i]] = []

        levels = 0
        while  frontier:
            if end in frontier:
                return levels
            newfrontier = {j for i in frontier for j in next_states(i)}
            reached.update(frontier)
            frontier = newfrontier.difference(reached)
            levels += 1

        return levels
                