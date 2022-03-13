#User function Template for python3

class Solution:
    def moveUp(arr, val):
        i = len(arr)-1
        while arr[self.getParent(i)] and arr[val]<arr[self.getParent(i)]:
            arr[val],arr[self.getParent(i)] = arr[self.getParent(i)], arr[val]
            val = arr[self.getParent(i)]
            i = self.getParent(i)
        return arr
    def insert(self, arr, val):
        i = len(arr)
        arr.append(val)
        while arr[self.getParent(i)] and arr[val]<arr[self.getParent(i)]:
            arr[val],arr[self.getParent(i)] = arr[self.getParent(i)], arr[val]
            val = arr[self.getParent(i)]
            i = self.getParent(i)
    # the parent
    def getParent(self,arr, index):
        if index == 0:
            return None
        return (index-1)//2
    # right child
    def rightChild(self, index):
        return 2*index+2
    # left child
    def leftChild(self, index):
        return 2*index+1
    def downHeap(self,arr, n, i):
        larg = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            larg = l
        if r < n and arr[larg] < arr[r]:
            larg = r
        if larg != i:
            arr[i], arr[larg] = arr[larg], arr[i]
            self.downHeap(arr, n, larg)
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        self.heapify(arr, n)
        
    def heapify(self,arr, n):
        for i in range(n//2, -1, -1):
            self.downHeap(arr, n, i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.heapify(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.downHeap(arr, i, 0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends