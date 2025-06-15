## Heap Data Structure
https://www.youtube.com/watch?v=4BfL2Hjvh8g&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=2
### Core Concepts
- **Definition**: A complete binary tree that satisfies the heap property
- **Types**:
  - Max Heap: Parent node is always greater than or equal to its children
  - Min Heap: Parent node is always less than or equal to its children
- **Properties**:
  - Complete binary tree (filled from left to right)
  - Height: O(log n)
  - Root is always the maximum (max heap) or minimum (min heap)

### Implementation Details
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._bubble_up(parent)
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val
    
    def _bubble_down(self, i):
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right
            
        if min_idx != i:
            self.swap(i, min_idx)
            self._bubble_down(min_idx)
```

### Time Complexities
- Insert: O(log n)
- Extract Min/Max: O(log n)
- Get Min/Max: O(1)
- Build Heap: O(n)

### Common Applications
1. **Priority Queues**
   - Task scheduling
   - Event-driven simulation
   - Dijkstra's algorithm

2. **Heap Sort**
   - In-place sorting algorithm
   - O(n log n) time complexity

3. **K-th Element Problems**
   - Find k-th largest/smallest element
   - Merge k sorted lists

### Must-Solve Heap Problems
1. **Basic Operations**
   - Implement a min/max heap
   - Heapify an array
   - Merge k sorted lists

2. **K-th Element Problems**
   - Find k-th largest element in array
   - Find median from data stream
   - Top k frequent elements

3. **Priority Queue Applications**
   - Task scheduler
   - Meeting rooms II
   - Merge k sorted lists

### Common Patterns
1. **Two Heap Pattern**
   - Maintain two heaps (min and max)
   - Useful for finding median
   - Example: Median of data stream

2. **K-element Heap**
   - Keep only k elements in heap
   - Useful for top-k problems
   - Example: Top k frequent elements

3. **Heap + Hash Map**
   - Track frequencies with hash map
   - Use heap for ordering
   - Example: Top k frequent words

### Tips & Tricks
1. **Python's heapq Module**
   - Default implementation is min heap
   - Use negative numbers for max heap
   - `heapq.heapify()`, `heapq.heappush()`, `heapq.heappop()`

2. **Common Mistakes**
   - Forgetting to heapify after modifications
   - Not handling empty heap cases
   - Incorrect comparison in custom objects

3. **Optimization Techniques**
   - Use heapify for O(n) initialization
   - Consider space-time tradeoffs
   - Use appropriate heap type (min/max)

### Interview Preparation
1. **Key Concepts to Master**
   - Heap property and maintenance
   - Heapify process
   - Priority queue operations

2. **Common Variations**
   - Custom comparator heaps
   - Indexed heaps
   - Binomial heaps

3. **Problem-Solving Approach**
   - Identify if problem needs ordering
   - Consider if k-th element is involved
   - Check if priority queue is needed 