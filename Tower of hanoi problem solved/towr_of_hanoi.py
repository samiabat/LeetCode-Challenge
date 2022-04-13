def tower_of_hanoi(n):
    def helper(n , left, center, right): 
        if n<0:
            return
        helper(n-1, left, right, center) 
        print ("Move disk",n,"from",left,"to",center)
        helper(n-1, right, center, left) 
    helper(n, "left", "center", "right")  
tower_of_hanoi(5)
