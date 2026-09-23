# 2. Add Two Numbers

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Topic](https://img.shields.io/badge/Topic-Linked%20List-blue?style=flat-square)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20Link-orange?style=flat-square&logo=leetcode)](https://leetcode.com/problems/add-two-numbers/)

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

### Example 1
```text
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2
```text
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3
```text
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

---

## Constraints

* The number of nodes in each linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros.

---

## Approach & Intuition

* **Simulation**: Simulate digit-by-digit addition just like grade-school elementary math.
* Keep a `carry` variable tracking values $\ge 10$.
* Traverse both lists concurrently while either list has nodes or `carry != 0`.
* Use a **dummy head** node to simplify linked list creation and boundary checks.
* Delete the dummy pointer in C++ to avoid memory leaks before returning `dummy->next`.

### Complexity
* **Time Complexity**: $\mathcal{O}(\max(m, n))$, where $m$ and $n$ are the lengths of `l1` and `l2`.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output linked list).
