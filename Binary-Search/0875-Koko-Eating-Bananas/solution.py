from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary Search on the Answer.
        
        Search space: speed k in range [1, max(piles)].
        Time Complexity: O(N * log(max(piles)))
        Space Complexity: O(1)
        """
        left = 1
        right = max(piles)
        best_speed = right

        while left <= right:
            mid = left + (right - left) // 2

            # Total hours required at speed `mid` using integer ceiling division
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                best_speed = mid
                right = mid - 1  # Can we eat slower? Search left half
            else:
                left = mid + 1   # Too slow, need faster speed
                
        return best_speed
