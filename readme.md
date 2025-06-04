The exercises in the following slides are designed to support learning and are a great help in preparing for the final exam. The more challenging exercises also serve as an in-depth exploration for those who wish to deepen their understanding beyond the core material

1. Write a function that checks whether a given string of brackets is balanced. Examples:
    
    ```python
    ([]{}) → True
    ([)] → False
    ((())) → True
    ```
    
    The solution must use a stack explicitly
    
2. Explain what hash tables are and how they differ from a list and a set. Provide a real-world example where using a hash table would be more efficient than other data structures
3. Define the following types of graphs, highlighting key differences and giving at least one possible use case for each:
    - directed graph
    - weighted graph
    - cyclic graph
    - bipartite graph
4. Explain the differences in terms of time complexity, space complexity, and stability between at least three sorting algorithms (e.g., Bubble Sort, Merge Sort, Quick Sort). For each of the following cases, identify which algorithm would be the most suitable and why:
    - An already sorted input
    - A reversed input
    - Input containing many duplicates
    - Very large input (millions of elements)
5. Write a Python function that, given a singly linked list of integers sorted in increasing order, removes all duplicates, keeping only one copy of each value. Example:
    
    ```python
    Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
    Output: 1 -> 2 -> 3 -> 4 -> 5
    ```
    
6. Write a Python function that implements the Merge Sort algorithm. Include comments explaining how the algorithm works step-by-step. Optionally, discuss its time and space complexity
7. Analyze the time and space complexity of the following algorithm. Use Big-O notation and justify your answer
    
    ```python
    def rearrange_list(data):
    	result = []
    	for i in range(len(data)):
    		for j in range(i, len(data)): 
    			result.append(data[j])
    		data = data[1:]
    	return result
    ```
    
8. Write a Python function that, given a binary tree (not necessarily a binary search tree), returns the sum of the values stored in all nodes at even depth levels (level 0, 2, 4, ...). Briefly justify your choice of traversal method (recursion or queue)
9. Given a list of non-negative integers, write a function to determine if it is possible to reach the last index starting from index 0. Each value in the list represents the maximum number of steps you can jump forward from that position. Examples:
    
    ```python
    Input: [3, 2, 1, 0, 4] -> Output: False
    Input: [2, 3, 1, 1, 4] -> Output: True
    ```
    
10. You are given two queues. Write a Python class that uses only these two queues to simulate a stack. Implement both push and pop operations
11. Describe how Dijkstraʼs algorithm works. What is the main difference compared to Bellman-Ford? Then implement Dijkstraʼs algorithm in Python using a dictionary to represent the graph and a priority queue for node selection
12. Write a function that returns the length of the longest path in a binary tree (not necessarily balanced or a BST), where the path can start and end at any node and must go through parent-child connections
13. Given an array of characters, return a string where the characters are sorted by decreasing frequency. Example:

```python
Input: ['a', 'b', 'a', 'c', 'a', 'b']
Output: "aaabbc"
```

Hint: Use a hash table to count frequencies, then sort by frequency

14. For each of the following sorting algorithms, state whether it is stable or unstable, and explain what "stability" means in the context of sorting algorithms:
    - Bubble Sort
    - Insertion Sort
    - Quick Sort
    - Heap Sort
    - Merge Sort