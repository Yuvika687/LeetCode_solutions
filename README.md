# 🧠 Data Structures & Algorithms — LeetCode Solutions

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,11,21&height=180&section=header&text=DSA%20%26%20LeetCode%20Hub&fontSize=50&fontColor=ffffff&animation=fadeIn" alt="Header" width="100%" />
</p>

<p align="center">
  <strong>Curated, optimized solutions to LeetCode and DSA problems with complexity analyses and clean code.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Total%20Solved-4-brightgreen?style=for-the-badge&logo=leetcode&logoColor=white" alt="Solved" />
  <img src="https://img.shields.io/badge/Easy-1-00b8a3?style=for-the-badge" alt="Easy" />
  <img src="https://img.shields.io/badge/Medium-3-ffc01e?style=for-the-badge" alt="Medium" />
  <img src="https://img.shields.io/badge/Hard-0-ff375f?style=for-the-badge" alt="Hard" />
  <img src="https://img.shields.io/badge/Languages-C++%20|%20Python-informational?style=for-the-badge" alt="Languages" />
  <img src="https://img.shields.io/badge/Daily%20Streak-Active%20🔥-critical?style=for-the-badge" alt="Streak" />
</p>

---

## 📌 Philosophy & Daily Consistency

> *"We are what we repeatedly do. Excellence, then, is not an act, but a habit."* — Will Durant

This repository is maintained daily as part of deliberate practice for coding interviews, problem-solving mastery, and clean software craftsmanship. Every problem is categorized by topic and accompanied by:
- 💡 **Intuition & Approach**: Why this technique works.
- ⏱️ **Time & Space Complexity**: Big-$\mathcal{O}$ analysis.
- 🧼 **Clean & Idiomatic Code**: Written following industry standards.

---

## 🗂️ Topic Breakdown

| Topic | Solved | Status |
| :--- | :---: | :---: |
| 🗃️ [Arrays & Hashing](./Arrays-and-Hashing/) | 1 | 🟢 Active |
| 🔗 [Linked List](./Linked-List/) | 1 | 🟢 Active |
| 🎯 [Binary Search](./Binary-Search/) | 1 | 🟢 Active |
| 👥 [Two Pointers](./Two-Pointers/) | 1 | 🟢 Active |
| 🪟 Sliding Window | 0 | ⚪ Planned |
| 📚 Stack | 0 | ⚪ Planned |
| 🌲 Trees & Tries | 0 | ⚪ Planned |
| 🏔️ Heap / Priority Queue | 0 | ⚪ Planned |
| 🌐 Graphs & BFS/DFS | 0 | ⚪ Planned |
| 🧩 Dynamic Programming | 0 | ⚪ Planned |
| 💰 Greedy | 0 | ⚪ Planned |

---

## 📑 Master Problem Log

| # | Problem | Difficulty | Category | Language | Solution | Date Solved |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: |
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | `Easy` | Arrays & Hashing | C++ | [View](./Arrays-and-Hashing/0001-Two-Sum/) | 2026-09-21 |
| 0002 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | `Medium` | Linked List | C++ | [View](./Linked-List/0002-Add-Two-Numbers/) | 2026-09-21 |
| 0875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | `Medium` | Binary Search | Python | [View](./Binary-Search/0875-Koko-Eating-Bananas/) | 2026-09-21 |
| 0881 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | `Medium` | Two Pointers | Python | [View](./Two-Pointers/0881-Boats-to-Save-People/) | 2026-09-22 |

---

## 📂 Repository Architecture

```bash
LeetCode_solutions/
├── Arrays-and-Hashing/
│   └── 0001-Two-Sum/
│       ├── README.md           # Problem notes & complexity analysis
│       └── solution.cpp        # Clean C++ implementation
├── Binary-Search/
│   └── 0875-Koko-Eating-Bananas/
│       ├── README.md
│       └── solution.py         # Python binary search implementation
├── Linked-List/
│   └── 0002-Add-Two-Numbers/
│       ├── README.md
│       └── solution.cpp
├── Two-Pointers/
│   └── 0881-Boats-to-Save-People/
│       ├── README.md
│       └── solution.py
├── scripts/
│   └── new_problem.py          # CLI scaffolder for rapid creation
└── README.md
```

---

## ⚡ Developer Workflow (Scaffolding New Solutions)

A custom CLI tool is included in `scripts/new_problem.py` to auto-generate standardized problem folders, boilerplate code, and documentation badges.

### Interactive Mode:
```bash
python3 scripts/new_problem.py
```

### One-Liner Flag Mode:
```bash
python3 scripts/new_problem.py \
  --number 121 \
  --title "Best Time to Buy and Sell Stock" \
  --topic "Sliding-Window" \
  --difficulty "Easy" \
  --lang "py"
```

---

## 🏷️ Commit Message Standard

To keep git history clean and professional:

* `feat(0001): solve Two Sum in C++ with hash map [O(n)]`
* `feat(0875): solve Koko Eating Bananas with binary search [O(n log m)]`
* `refactor(0002): optimize dummy head cleanup in Add Two Numbers`
* `docs: update master log table and badges`

---

<p align="center">
  Crafted with care by <strong><a href="https://github.com/Yuvika687">Yuvika Malhotra</a></strong> • Keep Grinding 🚀
</p>