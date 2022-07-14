class Solution:
    def lastRemaining(self, n: int) -> int:
        operations = []
        passesCount = 0
        while n > 3:
            
            if n%2 == 0 and passesCount%2 == 1:
                operations.append(1)
            operations.append(2)
            n = n // 2
            passesCount += 1
    
        last = 0
        if n == 3 or (n == 2 and passesCount%2 == 0):
            last = 2
        else:
            #if n == 1 or (n == 2 and passesCount%2 == 1):
            last = 1
        
        
        for i in range(len(operations)-1, -1, -1):
            if operations[i] == 2:
                last *= 2
            else:
                last -= 1
        return last
#     def lastRemaining(self, n: int) -> int:
#         if n == 1:
#             return 1
#         def rec(n):
#             if len(arr)==1:
#                 return arr[0]
#             arr = arr[::-1]
#             arr = [arr[i] for i in range(len(arr)) if i%2]
#             return rec(arr)
#         return rec(arr)


            