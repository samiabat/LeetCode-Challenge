from string import ascii_lowercase as ascii

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        pq = [c for c in reversed(ascii) if count[c]]
        result =  t = ''

        for c in s:
            while count[pq[-1]] == 0: pq.pop()

            while t and t[-1] <= pq[-1]:
                result += t[-1]
                t = t[:-1]

            if c == pq[-1]: result += c
            else: t += c
                
            count[c] -= 1

        result += t[::-1]
        return result