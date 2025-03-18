# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] 
# bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, 
# she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and 
# will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the 
# bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find minimum time to finish eating all bananas before guards come back

        # binary search over all valid rates
        low = 1
        high = max(piles)
        while low < high:
            rate = (low + high) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile/rate)

            if time_to_eat > h:
                low = rate + 1
            else:
                high = rate

        return low
    
# Time complexity: O(nlog(max(piles)))
# Space complexity: O(1)