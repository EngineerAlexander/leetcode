# There are n cars at given miles away from the starting mile 0, 
# traveling to reach the mile target.
# You are given two integer array position and speed, both of 
# length n, where position[i] is the starting mile of the ith 
# car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel 
# next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other. 
# The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still 
# be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.
# Constraints:
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort to start at front
        z = zip(position, speed)
        
        # build up a stack of only increasing arrival times. number will be number of fleets
        fleet_stack = []
        for car in sorted(z)[::-1]:
            pos = car[0]
            speed = car[1]

            time = (target-pos)/speed
            if (not fleet_stack) or (time > fleet_stack[-1]):
                fleet_stack.append(time)

        return len(fleet_stack)

# Time complexity: O(nlog(n))
# Space complexity: O(n)