class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            destroyed = False
            if len(stack) == 0:
                stack.append(asteroids[i])
                continue
            
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                a = abs(stack[-1])
                b = abs(asteroids[i])

                if a == b:
                    destroyed = True
                    stack.pop()
                    break
                elif a < b:
                    stack.pop()
                else:
                    destroyed = True
                    break
            if not destroyed:
                stack.append(asteroids[i])
        return stack
