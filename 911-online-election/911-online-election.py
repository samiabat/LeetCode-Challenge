class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        votes, self.winner = defaultdict(int), defaultdict(int)
        current_leader = None
        for i in range(len(persons)):
            votes[persons[i]] += 1
            if  current_leader == None or votes[persons[i]] >= votes[current_leader]:
                current_leader = persons[i]
            self.winner[times[i]] = current_leader
            
    def q(self, t: int) -> int:
        l = 0
        r = len(self.times)-1
        while l<=r:
            m = (l+r)//2
            if self.times[m]>t:
                r = m-1
            elif self.times[m]<t:
                l = m+1
            else:
                l=m+1
                break
        return self.winner[self.times[l-1]]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)