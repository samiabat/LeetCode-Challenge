class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        next_loc={'n':(0,1),'s':(0,-1),'e':(1,0),'w':(-1,0)}
        
        mapping={
        'n':['w','e'],
        's':['e','w'],
        'e':['n','s'],
        'w':['s','n']
        }

        origin=(0,0)
        curr_loc=(0,0)

        facing_dir='n'

        for i in instructions:
            if i=='L':
                facing_dir=mapping[facing_dir][0]
            elif i=='R':
                facing_dir=mapping[facing_dir][1]
            elif i=='G':
                x,y=next_loc[facing_dir]
                curr_loc=(curr_loc[0]+x,curr_loc[1]+y)
        if curr_loc==origin or facing_dir!='n':
            return True
        return False