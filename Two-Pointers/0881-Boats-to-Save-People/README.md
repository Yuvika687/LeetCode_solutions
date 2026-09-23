# 881. Boats to Save People

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Topic](https://img.shields.io/badge/Topic-Two%20Pointers-blue?style=flat-square)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20Link-orange?style=flat-square&logo=leetcode)](https://leetcode.com/problems/boats-to-save-people/)

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the `i-th` person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return *the minimum number of boats to carry every given person*.

---

### Example 1
```text
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

### Example 2
```text
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

### Example 3
```text
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

---

## Constraints

* `1 <= people.length <= 5 * 10^4`
* `1 <= people[i] <= limit <= 3 * 10^4`

---

## Approach & Intuition: Greedy + Two Pointers

* **Greedy Strategy**: To minimize boats, we should maximize the number of pairs sharing a boat.
* Sort the `people` array in ascending order.
* Use two pointers:
  * `left` pointing to the lightest remaining person.
  * `right` pointing to the heaviest remaining person.
* If `people[left] + people[right] <= limit`, both can share a boat $\rightarrow$ advance `left`.
* Regardless, the heaviest person `right` must take this boat $\rightarrow$ decrement `right`.
* Increment the `boats` count in each step until all people are rescued.

### Complexity
* **Time Complexity**: $\mathcal{O}(n \log n)$ due to sorting.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space if sorted in place.
