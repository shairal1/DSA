# Tree Data Structure Interview Guide

## Tree Types Visualization

### Balanced vs Unbalanced Binary Tree
![Balanced vs Unbalanced Binary Tree](https://media.geeksforgeeks.org/wp-content/uploads/20240805164549/balance-vs-unbalance-binnary-tree.webp)

### Balanced Tree Properties
- Height difference between left and right subtrees ≤ 1
- Number of nodes at each level is maximized
- Height is approximately log(n)

### Unbalanced Tree Properties
- Height difference between subtrees > 1
- Can degenerate into a linked list
- Height can be O(n)

## Unbalanced Tree Examples

### Types of Unbalanced Trees

1. **Left Skewed Tree**
```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

2. **Right Skewed Tree**
```
1
/
2
/
3
/
4
/
5
```

3. **Partially Unbalanced Tree**
```
     1
    / \
   2   3
  /     \
 4       5
/         \
6          7
```

### Impact on Performance

1. **Time Complexity**:
   ```python
   # Balanced Tree (O(log n))
   def search_balanced(root, target):
       if not root:
           return False
       if root.val == target:
           return True
       if target < root.val:
           return search_balanced(root.left, target)
       return search_balanced(root.right, target)
   
   # Unbalanced Tree (O(n))
   def search_unbalanced(root, target):
       if not root:
           return False
       if root.val == target:
           return True
       return search_unbalanced(root.left, target) or \
              search_unbalanced(root.right, target)
   ```

2. **Space Complexity**:
   ```python
   # Balanced Tree (O(log n) stack space)
   def height_balanced(root):
       if not root:
           return 0
       return 1 + max(height_balanced(root.left),
                     height_balanced(root.right))
   
   # Unbalanced Tree (O(n) stack space)
   def height_unbalanced(root):
       if not root:
           return 0
       return 1 + height_unbalanced(root.left)  # Always goes left
   ```

### Common Causes of Unbalanced Trees

1. **Insertion Order**:
   ```python
   # Creates a right-skewed tree
   root = TreeNode(1)
   for i in range(2, 6):
       root.right = TreeNode(i)
       root = root.right
   
   # Creates a balanced tree
   root = TreeNode(3)
   root.left = TreeNode(2)
   root.right = TreeNode(4)
   root.left.left = TreeNode(1)
   root.right.right = TreeNode(5)
   ```

2. **Deletion Without Rebalancing**:
   ```python
   # Can create imbalance
   def delete_without_rebalance(root, key):
       if not root:
           return None
       if key < root.val:
           root.left = delete_without_rebalance(root.left, key)
       elif key > root.val:
           root.right = delete_without_rebalance(root.right, key)
       else:
           if not root.left:
               return root.right
           if not root.right:
               return root.left
           # Find successor
           temp = root.right
           while temp.left:
               temp = temp.left
           root.val = temp.val
           root.right = delete_without_rebalance(root.right, temp.val)
       return root
   ```

### Solutions for Unbalanced Trees

1. **Self-Balancing Trees**:
   - AVL Trees
   - Red-Black Trees
   - B-Trees

2. **Rebalancing Operations**:
   ```python
   def rebalance_tree(root):
       # Get sorted nodes
       nodes = []
       def inorder(root):
           if root:
               inorder(root.left)
               nodes.append(root)
               inorder(root.right)
       
       # Build balanced tree
       def build_balanced(start, end):
           if start > end:
               return None
           mid = (start + end) // 2
           root = nodes[mid]
           root.left = build_balanced(start, mid - 1)
           root.right = build_balanced(mid + 1, end)
           return root
       
       inorder(root)
       return build_balanced(0, len(nodes) - 1)
   ```

### Performance Comparison

| Operation | Balanced Tree | Unbalanced Tree |
|-----------|--------------|-----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Space | O(log n) | O(n) |

## How to Calculate Time & Space Complexity

### Time Complexity Calculation
[Video Tutorial](https://www.youtube.com/watch?v=XZQKgcjbogo)

1. **Basic Formula**: Work done per node × Number of nodes = 2^h (in balanced trees)
   - Work done per node: Operations performed at each node
   - Number of nodes: Total nodes in the tree
   - In balanced trees: n ≈ 2^h where h is height

2. **Common Patterns**:
   - Single traversal: O(n)
   - Multiple traversals: O(n × number of traversals)
   - Height-based operations: O(h) where h is height
   - Balanced tree: h = log(n)
   - Skewed tree: h = n

3. **Examples**:
   ```python
   # O(n) - Single traversal
   def inorder_traversal(root):
       if root:
           inorder_traversal(root.left)    # O(n/2)
           process(root)                   # O(1)
           inorder_traversal(root.right)   # O(n/2)
   
   # O(n²) - Multiple traversals
   def diameter_of_binary_tree(root):
       if not root:
           return 0
       # O(n) for height calculation
       left_height = height(root.left)     # O(n)
       right_height = height(root.right)   # O(n)
       # O(n) for recursive calls
       return max(left_height + right_height,
                 diameter_of_binary_tree(root.left),
                 diameter_of_binary_tree(root.right))
   ```

### Space Complexity Calculation
1. **Basic Formula**: Maximum space used at any point
   - Recursion stack: O(h) where h is height
   - Extra space: O(k) where k is additional space needed

2. **Common Patterns**:
   - Recursive calls: O(h)
   - Level order traversal: O(w) where w is max width
   - Path storage: O(h)
   - Node tracking: O(n)

3. **Examples**:
   ```python
   # O(h) - Recursion stack
   def max_depth(root):
       if not root:
           return 0
       return 1 + max(max_depth(root.left),
                     max_depth(root.right))
   
   # O(w) - Queue for level order
   def level_order(root):
       queue = [root]          # O(w) space
       while queue:
           node = queue.pop(0)
           if node.left:
               queue.append(node.left)
           if node.right:
               queue.append(node.right)
   ```

### Complexity Cheat Sheet

| Operation | Time | Space | Why |
|-----------|------|-------|-----|
| Traversal | O(n) | O(h) | Visit each node once, stack height = tree height |
| Search BST | O(h) | O(1) | Follow path to target, no extra space |
| Insert BST | O(h) | O(1) | Follow path to insert point, no extra space |
| Delete BST | O(h) | O(1) | Find node + rebalance, no extra space |
| Height | O(n) | O(h) | Visit all nodes, stack height = tree height |
| Path Sum | O(n) | O(h) | Visit all nodes, stack height = tree height |
| LCA | O(n) | O(h) | Visit all nodes, stack height = tree height |

### Tips for Complexity Analysis
1. **Count Operations**:
   - How many times is each node visited?
   - What operations are performed per visit?
   - Are there nested traversals?

2. **Consider Space**:
   - Recursion stack depth
   - Extra data structures
   - Path storage
   - Node tracking

3. **Special Cases**:
   - Balanced vs Skewed trees
   - BST vs Binary Tree
   - Complete vs Incomplete trees

## Must-Solve Tree Problems for Interviews

### 1. Fundamental Tree Problems (High Priority)
- [x] Binary Tree Level Order Traversal
- [x] Validate Binary Search Tree
- [x] Balanced Binary Tree
- [x] Binary Tree Maximum Path Sum
- [x] Lowest Common Ancestor (LCA)
- [x] Construct Binary Tree from Inorder and Preorder/Postorder

### 2. BST Operations (High Priority)
- [x] Find kth Smallest Element in BST
- [x] Inorder Successor in BST
- [x] Convert Sorted Array to Balanced BST
- [x] Recover Binary Search Tree (Fix Swapped Nodes)
- [x] Delete Node in BST

### 3. Tree Traversal Variations (Medium Priority)
- [x] Binary Tree Zigzag Level Order Traversal
- [x] Binary Tree Right Side View
- [x] Binary Tree Vertical Order Traversal
- [x] Binary Tree Boundary Traversal

### 4. Path and Sum Problems (Medium Priority)
- [x] Path Sum I, II, III
- [x] Binary Tree Longest Consecutive Sequence
- [x] Diameter of Binary Tree
- [x] Sum Root to Leaf Numbers

### 5. Tree Construction (Medium Priority)
- [x] Serialize and Deserialize Binary Tree
- [x] Construct Binary Tree from String
- [x] Convert BST to Greater Tree

### 6. Tree Properties (Low Priority)
- [x] Symmetric Tree
- [x] Invert Binary Tree
- [x] Subtree of Another Tree
- [x] Binary Tree Tilt

### Problem-Solving Strategy
1. **Start with High Priority Problems**: These are the most commonly asked questions
2. **Understand the Patterns**: 
   - Tree traversal (DFS/BFS)
   - Recursive vs Iterative solutions
   - Path finding techniques
   - BST property utilization
3. **Time Complexity Focus**:
   - Most tree problems should be solved in O(n) time
   - Space complexity is usually O(h) for recursion or O(n) for level order
4. **Common Patterns**:
   - Use DFS for path problems
   - Use BFS for level-order problems
   - Use BST properties for search operations
   - Use recursion for tree construction

### Quick Tips
1. Always check for null nodes first
2. Consider both recursive and iterative solutions
3. For BST problems, utilize the BST properties
4. For path problems, consider backtracking
5. For level order, use queue-based BFS
6. For vertical order, use hashmap with horizontal distance

## Essential Tree Problem Types

### 1. Core Tree Construction & Traversal
- Construct BST from sorted array
- Construct tree from inorder and preorder/postorder
- Morris traversal (without stack/recursion)
- Level order traversal with level separation
- Vertical order traversal
- Boundary traversal

### 2. Tree Properties & Validation
- Check if tree is balanced
- Check if tree is symmetric
- Check if tree is complete
- Find diameter of tree
- Find maximum path sum
- Find lowest common ancestor (LCA)

### 3. BST Specific Operations
- Find kth smallest/largest element
- Find inorder successor/predecessor
- Find floor and ceiling
- Validate BST
- Recover BST (fix swapped nodes)
- Convert BST to balanced BST

### 4. Tree Path & Sum Problems
- Find all root-to-leaf paths
- Find path with given sum
- Find maximum path sum
- Find longest consecutive sequence
- Find nodes at k distance
- Find distance between nodes

### 5. Tree Serialization & Deserialization
- Serialize and deserialize binary tree
- Serialize and deserialize BST
- Serialize and deserialize with null markers
- Serialize and deserialize with level order

### 6. Advanced Tree Concepts
- Threaded Binary Tree
- Expression Tree
- Trie (Prefix Tree)
- Segment Tree
- B-Tree
- Red-Black Tree

### 7. Tree Applications
- File system representation
- XML/HTML parsing
- Expression evaluation
- Decision tree
- Game tree
- Syntax tree

## Additional Tree Question Types

### 1. Tree Construction Problems
- Construct BST from sorted array
- Construct tree from inorder and preorder
- Construct tree from inorder and postorder
- Construct tree from level order
- Construct tree from string representation
- Convert sorted array to balanced BST
- Convert BST to balanced BST

### 2. Tree Modification Problems
- Invert/Mirror a binary tree
- Flatten binary tree to linked list
- Delete nodes with given value
- Prune tree (remove subtrees with given condition)
- Merge two binary trees
- Convert BST to greater sum tree
- Convert binary tree to its mirror

### 3. Tree Path Problems
- Print all root-to-leaf paths
- Find path with maximum sum
- Find path with given sum
- Find longest path between two nodes
- Find shortest path between two nodes
- Find all paths that sum to target
- Find paths with maximum average

### 4. Tree View Problems
- Left view of binary tree
- Right view of binary tree
- Top view of binary tree
- Bottom view of binary tree
- Diagonal view of binary tree
- Vertical order traversal
- Boundary traversal

### 5. Tree Property Problems
- Check if tree is complete
- Check if tree is full
- Check if tree is perfect
- Check if tree is symmetric
- Check if tree is balanced
- Find diameter of tree
- Find width of tree

### 6. BST Specific Problems
- Find kth smallest element
- Find kth largest element
- Find inorder successor
- Find inorder predecessor
- Find floor and ceiling
- Find closest value
- Find range sum

### 7. Tree Serialization Problems
- Serialize and deserialize binary tree
- Serialize and deserialize BST
- Serialize and deserialize N-ary tree
- Serialize and deserialize with null markers
- Serialize and deserialize with level order

### 8. Tree Traversal Variations
- Morris traversal (without stack/recursion)
- Spiral/Zigzag traversal
- Reverse level order traversal
- Diagonal traversal
- Vertical order traversal
- Boundary traversal
- Level order with level separation

### 9. Tree Comparison Problems
- Check if two trees are identical
- Check if one tree is subtree of another
- Check if two trees are mirror
- Check if two trees are isomorphic
- Find common ancestors
- Find distance between nodes
- Find nodes at k distance

### 10. Advanced Tree Problems
- Binary Tree Cameras
- Recover Binary Search Tree
- Binary Tree Maximum Path Sum
- Binary Tree Pruning
- Binary Tree Coloring Game
- Binary Tree Tilt
- Binary Tree Longest Consecutive Sequence

### 11. Tree with Parent Pointer
- Find inorder successor with parent
- Find inorder predecessor with parent
- Find LCA with parent pointer
- Find distance between nodes with parent
- Find next right node
- Find next node at same level
- Find nodes at k distance with parent

### 12. Tree with Multiple Children
- N-ary tree traversals
- N-ary tree level order
- N-ary tree serialization
- N-ary tree LCA
- N-ary tree path sum
- N-ary tree maximum depth
- N-ary tree diameter

### 13. Tree with Special Properties
- Threaded Binary Tree
- Expression Tree
- Segment Tree
- Fenwick Tree
- Trie (Prefix Tree)
- Suffix Tree
- B-Tree

### 14. Tree Optimization Problems
- Optimize tree height
- Optimize tree balance
- Optimize tree storage
- Optimize tree traversal
- Optimize tree search
- Optimize tree insertion
- Optimize tree deletion

### 15. Tree Application Problems
- File system representation
- XML/HTML parsing
- Expression evaluation
- Decision tree
- Game tree
- Syntax tree
- Abstract syntax tree
