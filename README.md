# Weighted Interval Scheduling (WIS)

This project implements and compares two approaches for solving the **Weighted Interval Scheduling** problem:

1. **Naive Recursive Algorithm**
2. **Optimized Dynamic Programming Algorithm (with Binary Search)**

The project also includes an **empirical runtime analysis** to demonstrate the performance difference between the two approaches.

---

## 📌 Problem Description

Given a set of jobs, where each job has:
* `start time`
* `finish time`
* `profit`

The goal is to select a subset of **non-overlapping jobs** such that the **total profit is maximized**.

---

## 🧠 Algorithms Implemented

### 1️⃣ Naive Algorithm (Recursive)

* Tries **all possible combinations** of jobs.
* For each job:
  - Either **include** the job and move to the next non-conflicting job.
  - Or **exclude** the job and move to the next job.
* Guarantees a correct solution but is **not efficient**.

#### ⏱ Time Complexity
* **Exponential Time**:  
  \( O(2^n) \)
* Not suitable for large input sizes.

---

### 2️⃣ Optimized Algorithm (Dynamic Programming + Binary Search)

* Sorts jobs by **finish time**.
* Uses **Dynamic Programming** to store the maximum profit up to each job.
* Uses **Binary Search** to efficiently find the last non-conflicting job.

#### ⏱ Time Complexity
* Sorting: \( O(n log n) \)
* DP with Binary Search: \( O(n log n) \)
* **Overall:** \( O(n log n) \)

This approach is efficient and suitable for real-world applications.

---

## 📊 Empirical Analysis

The runtime of both algorithms was measured using randomly generated job sets of different sizes.

### Observations:
* The **naive algorithm** becomes extremely slow as `n` increases.
* The **optimized algorithm** scales efficiently even for very large inputs (up to 100,000 jobs).
* This confirms that **choosing the right algorithm is more important than just getting a correct answer**.

---

## 🛠 Technologies Used

* Python 3
* `time` module (runtime measurement)
* `random` module (test case generation)
* `bisect` module (binary search)

---

## ✅ Conclusion

* The naive solution is useful for understanding the problem.
* The optimized solution is practical and efficient.
* Performance analysis clearly shows the importance of algorithm optimization.
