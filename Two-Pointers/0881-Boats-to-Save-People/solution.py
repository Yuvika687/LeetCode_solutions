from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Greedy approach with Two Pointers.
        
        Strategy: Sort people by weight. Always pair the heaviest remaining 
        person with the lightest remaining person if their combined weight <= limit.
        Otherwise, the heaviest person must travel alone.
        
        Time Complexity: O(N log N)
        Space Complexity: O(1) auxiliary (in-place sort)
        """
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # If the lightest and heaviest person can share a boat
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always occupies a seat on this boat
            right -= 1
            boats += 1

        return boats
