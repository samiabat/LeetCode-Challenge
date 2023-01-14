class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        relations, d = [], dict() ## "relations" is a list of sets
        
        for c1,c2 in zip(s1,s2):
            if c1==c2: continue
            i1, i2 = None, None
            for i,r in enumerate(relations):
                if c1 in r or c2 in r:
                    if i1 is not None: ## two sets have the same character
                        i2 = i
                        relations[i1].update(r) ## merge the 2nd set to the 1st one
                        break
                    i1 = i
                    r.update((c1, c2))
            if i2 is not None:  ## delete the 2nd set
                relations = relations[:i2] + relations[i2+1:]
            if i1 is None:
                relations.append({c1, c2})

        for r in relations: ## convert to a dictionary so it is easier to work with
            l = sorted(r)
            for c in l:
                d[c] = l[0]
                
        return ''.join([d[c] if c in d else c for c in baseStr])