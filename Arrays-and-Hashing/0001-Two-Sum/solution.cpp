#include <vector>
#include <unordered_map>

class Solution {
public:
    // Optimal Solution: Hash Map (One-Pass)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> seen; // value -> index

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }

        return {};
    }

    // Alternative Brute-Force Solution
    // Time Complexity: O(n^2)
    // Space Complexity: O(1)
    std::vector<int> twoSumBruteForce(std::vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
