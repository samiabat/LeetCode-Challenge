class Solution:
    def racecar(self, target):
        stack, visited = collections.deque([(0,1,"")]), set()

        visited.add((0,1))

        while stack:
            position, speed, string = stack.popleft()

            if position == target:
                return len(string)

            if (position + speed,2*speed) not in visited:
                stack.append((position+speed,2*speed,string+"A"))
                visited.add((position+speed,2*speed))

            if speed > 0 and (position,-1) not in visited:
                stack.append((position,-1,string+"R"))
                visited.add((position,-1))

            if speed <= 0 and (position,1) not in visited:
                stack.append((position,1,string+"R"))
                visited.add((position,1))
