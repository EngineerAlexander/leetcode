# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning 
# right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids 
# meet, the smaller one will explode. If both are the same size, 
# both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0:
                    s.pop()
                elif s[-1] + a > 0:
                    break    
                else:
                    s.pop()
                    break
            else: s.append(a)        
        return s