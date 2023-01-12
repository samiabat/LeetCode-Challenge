#User function Template for python3

#User function Template for python3
from collections import defaultdict
def topoSort( V, adj):
        indeg=[0]*V
        ans=[]
        for i in range(V):
            for it in adj[i]:
                indeg[it]+=1
        queue=[]
        for i in range(V):
            if indeg[i]==0:
                queue.append(i)
        while queue:
            node=queue.pop()
            ans.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    queue.append(i)
        return ans
class Solution:
    def findOrder(self,dict, N, K):
        adj=defaultdict(list)
        for i in range(N-1):
            str1=dict[i]
            str2=dict[i+1]
            l=min(len(str1),len(str2))
            for i in range(l):
                if str1[i]!=str2[i]:
                    t=ord(str1[i])-ord('a')
                    s=ord(str2[i])-ord('a')
                    adj[t].append(s)
                    break
        topo=topoSort(K,adj)
        ans=''
        for it in topo:
            d=it+ord('a')
            ans+=chr(d)
        return ans
            
    # code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends