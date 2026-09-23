#!/usr/bin/env python3
"""
LeetCode Problem Scaffolder CLI
Author: Yuvika Malhotra
Usage:
    python3 scripts/new_problem.py
    python3 scripts/new_problem.py --number 121 --title "Best Time to Buy and Sell Stock" --topic "Sliding-Window" --difficulty "Easy" --lang "py"
"""

import os
import sys
import argparse
from datetime import date

TOPICS = [
    "Arrays-and-Hashing",
    "Two-Pointers",
    "Sliding-Window",
    "Stack",
    "Binary-Search",
    "Linked-List",
    "Trees",
    "Tries",
    "Heap-Priority-Queue",
    "Backtracking",
    "Graphs",
    "Advanced-Graphs",
    "1-D-Dynamic-Programming",
    "2-D-Dynamic-Programming",
    "Greedy",
    "Intervals",
    "Math-and-Geometry",
    "Bit-Manipulation",
]

DIFFICULTIES = ["Easy", "Medium", "Hard"]
EXTENSIONS = {
    "py": "solution.py",
    "cpp": "solution.cpp",
    "java": "Solution.java",
    "js": "solution.js",
    "ts": "solution.ts",
}

BOILERPLATE = {
    "py": '''from typing import List

class Solution:
    def solve(self):
        """
        Problem: {number}. {title}
        Difficulty: {difficulty}
        Topic: {topic}
        Date: {date}
        
        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        pass
''',
    "cpp": '''#include <iostream>
#include <vector>

/*
 * Problem: {number}. {title}
 * Difficulty: {difficulty}
 * Topic: {topic}
 * Date: {date}
 * 
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

class Solution {{
public:
    void solve() {{
        // Implementation
    }}
}};
''',
}

README_TEMPLATE = '''# {number}. {title}

![{difficulty}](https://img.shields.io/badge/Difficulty-{difficulty}-{diff_color}?style=flat-square)
![Topic](https://img.shields.io/badge/Topic-{topic_badge}-blue?style=flat-square)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20Link-orange?style=flat-square&logo=leetcode)]({slug_link})

## Problem Statement

<!-- Paste problem description here -->

---

## Constraints

<!-- Paste constraints here -->

---

## Approach & Intuition

* **Idea**: 
* **Time Complexity**: $\\mathcal{{O}}(?)$
* **Space Complexity**: $\\mathcal{{O}}(?)$
'''

DIFF_COLORS = {
    "Easy": "brightgreen",
    "Medium": "yellow",
    "Hard": "red",
}

def slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("'", "").replace('"', "")

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new LeetCode problem directory.")
    parser.add_argument("--number", type=int, help="Problem number, e.g. 1")
    parser.add_argument("--title", type=str, help="Problem title, e.g. 'Two Sum'")
    parser.add_argument("--topic", type=str, help=f"DSA Topic (e.g. {TOPICS[0]})")
    parser.add_argument("--difficulty", choices=DIFFICULTIES, help="Easy, Medium, or Hard")
    parser.add_argument("--lang", choices=list(EXTENSIONS.keys()), default="py", help="Language extension")

    args = parser.parse_args()

    # Interactive prompts if arguments are omitted
    num = args.number or int(input("Enter Problem Number (e.g. 1): ").strip())
    title = args.title or input("Enter Problem Title (e.g. Two Sum): ").strip()
    
    if not args.topic:
        print("\nSelect DSA Topic:")
        for idx, t in enumerate(TOPICS, 1):
            print(f"  [{idx:2d}] {t}")
        choice = int(input("Choose topic number: ").strip())
        topic = TOPICS[choice - 1]
    else:
        topic = args.topic

    if not args.difficulty:
        print("\nSelect Difficulty:")
        for idx, d in enumerate(DIFFICULTIES, 1):
            print(f"  [{idx}] {d}")
        choice = int(input("Choose difficulty number: ").strip())
        difficulty = DIFFICULTIES[choice - 1]
    else:
        difficulty = args.difficulty

    lang = args.lang

    # Format directory name: 0001-Two-Sum
    folder_name = f"{num:04d}-{title.replace(' ', '-')}"
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(repo_root, topic, folder_name)

    os.makedirs(target_dir, exist_ok=True)

    today = date.today().isoformat()
    slug_link = f"https://leetcode.com/problems/{slugify(title)}/"
    topic_badge = topic.replace("-", "%20")

    # Create README.md
    readme_path = os.path.join(target_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(README_TEMPLATE.format(
                number=num,
                title=title,
                difficulty=difficulty,
                diff_color=DIFF_COLORS[difficulty],
                topic_badge=topic_badge,
                slug_link=slug_link,
            ))
        print(f"✓ Created {readme_path}")

    # Create Solution file
    sol_file_name = EXTENSIONS.get(lang, "solution.py")
    sol_path = os.path.join(target_dir, sol_file_name)
    if not os.path.exists(sol_path):
        template = BOILERPLATE.get(lang, BOILERPLATE["py"])
        with open(sol_path, "w") as f:
            f.write(template.format(
                number=num,
                title=title,
                difficulty=difficulty,
                topic=topic,
                date=today,
            ))
        print(f"✓ Created {sol_path}")

    print(f"\n✨ Successfully scaffolded: {topic}/{folder_name}!")

if __name__ == "__main__":
    main()
