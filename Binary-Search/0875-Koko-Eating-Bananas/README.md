# 875. Koko Eating Bananas

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Topic](https://img.shields.io/badge/Topic-Binary%20Search-blue?style=flat-square)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20Link-orange?style=flat-square&logo=leetcode)](https://leetcode.com/problems/koko-eating-bananas/)

## Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer `k` such that she can eat all the bananas within `h` hours*.

---

### Example 1
```text
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 2
```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 3
```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

---

## Constraints

* `1 <= piles.length <= 10^4`
* `piles.length <= h <= 10^9`
* `1 <= piles[i] <= 10^9`

---

## Approach & Intuition: Binary Search on Answer

* Notice that the search space for the eating speed $k$ is monotonic:
  * Minimum possible speed: $1$ (if $h$ is very large).
  * Maximum possible speed: $\max(piles)$ (at this speed, each pile takes at most 1 hour).
* If Koko can finish all bananas at speed $k$, she can also finish at any speed $> k$.
* This monotonicity allows us to apply **Binary Search on the range $[1, \max(piles)]$**:
  * For a speed `mid`, calculate total hours needed: $\sum \lceil \frac{pile}{mid} \rceil$.
  * If `hours <= h`, record `mid` as a candidate and search the lower half (`right = mid - 1`).
  * If `hours > h`, Koko is eating too slowly, so search the upper half (`left = mid + 1`).

### Complexity
* **Time Complexity**: $\mathcal{O}(n \cdot \log(\max(piles)))$ where $n$ is `len(piles)`.
* **Space Complexity**: $\mathcal{O}(1)$ constant extra space.
