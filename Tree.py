"""
TREE INTERVIEW PREPARATION GUIDE
================================

1. ESSENTIAL TREE CONCEPTS
-------------------------
- write breaking conditions if root.left or root.right is None not when root is None, when root is None return or 0
- Binary Tree: Each node has at most 2 children
- Binary Search Tree (BST): Left subtree < Root < Right subtree
- Complete Binary Tree: All levels filled except possibly last, filled left to right
- Full Binary Tree: Each node has 0 or 2 children
- Perfect Binary Tree: All internal nodes have 2 children, all leaves at same level
- Balanced Tree: Height difference between left and right subtrees ≤ 1
!! Balanced tree is not the same as height balanced tree !!


2. COMMON INTERVIEW PATTERNS
---------------------------
A. Traversal Patterns:
   1. DFS (Depth-First Search)
      - Inorder (Left → Root → Right)
      - Preorder (Root → Left → Right)
      - Postorder (Left → Right → Root)
   2. BFS (Breadth-First Search)
      - Level Order
      - Zigzag/Spiral
      - Vertical Order

B. Tree Construction Patterns:
   1. From Traversal Combinations
      - Inorder + Preorder
      - Inorder + Postorder
      - Level Order + Inorder
   2. From Array/List
      - Sorted Array to BST
      - Level Order Array to Tree

C. Tree Property Patterns:
   1. Height/Depth Related
      - Maximum Depth
      - Minimum Depth
      - Balanced Check
   2. Path Related
      - Path Sum
      - Maximum Path Sum
      - Root to Leaf Paths

D. Tree Comparison Patterns:
   1. Symmetry Check
   2. Same Tree Check
   3. Subtree Check
   4. Lowest Common Ancestor (LCA)

3. COMMON INTERVIEW TRICKS
-------------------------
1. Use Global Variables for:
   - Tracking diameter
   - Storing maximum path sum
   - Keeping track of previous node in BST

2. Use Helper Functions for:
   - Recursive depth calculations
   - Path tracking
   - Node comparison

3. Use Stack/Queue for:
   - Iterative traversals
   - Level order operations
   - Path tracking

4. Use Hash Maps for:
   - Node value tracking
   - Level information
   - Path sum counting

4. TIME & SPACE COMPLEXITY GUIDE
------------------------------
Common Operations:
- Traversal: O(n) time, O(h) space (h = height)
- Search in BST: O(h) time, O(1) space
- Insert/Delete in BST: O(h) time, O(1) space
- Height Calculation: O(n) time, O(h) space
- Path Operations: O(n) time, O(h) space

5. COMMON INTERVIEW QUESTIONS BY DIFFICULTY
-----------------------------------------
Easy:
- Maximum Depth of Binary Tree
- Same Tree
- Symmetric Tree
- Invert Binary Tree
- Path Sum

Medium:
- Binary Tree Level Order Traversal
- Construct Binary Tree from Inorder and Preorder
- Lowest Common Ancestor
- Validate Binary Search Tree
- Binary Tree Right Side View

Hard:
- Serialize and Deserialize Binary Tree
- Binary Tree Maximum Path Sum
- Recover Binary Search Tree
- Binary Tree Cameras
- Vertical Order Traversal

6. IMPLEMENTATION TEMPLATES
--------------------------
"""

# TreeNode class definition
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 1. DFS TRAVERSAL TEMPLATES
    def inorder_traversal(self, root, result=None):
        """
        Inorder Traversal (Left → Root → Right)
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if result is None:
            result = []
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)
        return result

    def preorder_traversal(self, root, result=None):
        """
        Preorder Traversal (Root → Left → Right)
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if result is None:
            result = []
        if root:
            result.append(root.value)
            self.preorder_traversal(root.left, result)
            self.preorder_traversal(root.right, result)
        return result

    def postorder_traversal(self, root, result=None):
        """
        Postorder Traversal (Left → Right → Root)
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if result is None:
            result = []
        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.value)
        return result

    # 2. BFS TRAVERSAL TEMPLATE
    def levelorder_traversal(self, root):
        """
        Level Order Traversal (BFS)
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        result = []
        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                result.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def levelorder_traversal_with_levels(self, root):
        """
        Level Order Traversal with Level Separation
        Can be used for:
        1. Level Order Traversal
        2. Right Side View
        3. Left Side View
        4. Zigzag Level Order
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

    def right_side_view(self, root):
        """
        Right Side View of Binary Tree
        Returns the values of nodes visible from the right side
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.pop(0)
                
                # If it's the last node in the level, add to result
                if i == level_size - 1:
                    result.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

    def left_side_view(self, root):
        """
        Left Side View of Binary Tree
        Returns the values of nodes visible from the left side
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.pop(0)
                
                # If it's the first node in the level, add to result
                if i == 0:
                    result.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

    def zigzag_level_order(self, root):
        """
        Zigzag Level Order Traversal
        Returns level order traversal with alternating directions
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                
                # Add to current level based on direction
                if left_to_right:
                    current_level.append(node.value)
                else:
                    current_level.insert(0, node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
            left_to_right = not left_to_right
        
        return result

    def vertical_order_traversal(self, root):
        """
        Vertical Order Traversal
        Returns nodes in vertical order from left to right
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
            
        # Dictionary to store nodes by their horizontal distance
        vertical_map = {}
        # Queue to store (node, horizontal_distance)
        queue = [(root, 0)]
        min_hd = max_hd = 0
        
        while queue:
            node, hd = queue.pop(0)
            
            # Update min and max horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # Add node to the corresponding horizontal distance list
            if hd not in vertical_map:
                vertical_map[hd] = []
            vertical_map[hd].append(node.value)
            
            # Add children to queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Construct result by traversing from left to right
        result = []
        for hd in range(min_hd, max_hd + 1):
            if hd in vertical_map:
                result.append(vertical_map[hd])
        
        return result
#https://www.youtube.com/watch?v=-JFngYs21Y8
    def vertical_order_traversal_with_levels(self, root):
        """
        Vertical Order Traversal with Level Information
        Returns nodes in vertical order, and for same vertical line,
        nodes are ordered by their levels (top to bottom)
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n)
        """
        if not root:
            return []
            
        # Dictionary to store nodes by their horizontal distance
        vertical_map = {}
        # Queue to store (node, horizontal_distance, level)
        queue = [(root, 0, 0)]
        min_hd = max_hd = 0
        
        while queue:
            node, hd, level = queue.pop(0)
            
            # Update min and max horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # Add node to the corresponding horizontal distance list
            if hd not in vertical_map:
                vertical_map[hd] = []
            vertical_map[hd].append((level, node.value))
            
            # Add children to queue with updated horizontal distances and levels
            if node.left:
                queue.append((node.left, hd - 1, level + 1))
            if node.right:
                queue.append((node.right, hd + 1, level + 1))
        
        # Construct result by traversing from left to right
        result = []
        for hd in range(min_hd, max_hd + 1):
            if hd in vertical_map:
                # Sort by level and extract values
                vertical_map[hd].sort(key=lambda x: x[0])
                result.append([val for _, val in vertical_map[hd]])
        
        return result

    def sumNumbers(self, root):
        """
        Sum Root to Leaf Numbers
        Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
        could represent a number. Find the total sum of all root-to-leaf numbers.
        
        Example:
            1
           / \
          2   3
        Path 1->2 represents number 12
        Path 1->3 represents number 13
        Return: 12 + 13 = 25
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        def dfs(node, current_sum):
            if not node:
                return 0
                
            # Update current sum by multiplying by 10 and adding current node value
            current_sum = current_sum * 10 + node.value
            
            # If leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum
                
            # Recursively get sum from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)

    # 3. TREE PROPERTY TEMPLATES
    def maxDepth(self, root):
        """
        Maximum Depth of Binary Tree
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root):
        """
        Check if Tree is Balanced
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree
            - Best case (balanced tree): O(log n)
            - Worst case (skewed tree): O(n)
        """
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        
        return height(root) != -1

    # 4. PATH SUM TEMPLATE
    def hasPathSum(self, root, targetSum):
        """
        Path Sum Check
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.value
        return (self.hasPathSum(root.left, targetSum - root.value) or
                self.hasPathSum(root.right, targetSum - root.value))

    # 5. BST VALIDATION TEMPLATE
    def isValidBST(self, root):
        """
        Validate Binary Search Tree
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if node.value <= low or node.value >= high:
                return False
            return (validate(node.left, low, node.value) and
                    validate(node.right, node.value, high))
        
        return validate(root)

    # 6. LCA TEMPLATE https://www.youtube.com/watch?v=Oi3_06ultic
    def lowestCommonAncestor(self, root, p, q):
        """
        Lowest Common Ancestor
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left or right

    # 7. SERIALIZATION TEMPLATE
    def serialize(self, root):
        """
        Serialize Binary Tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return 'null'
        return f'#{root.value} {self.serialize(root.left)} {self.serialize(root.right)}'

    def deserialize(self, data):
        """
        Deserialize Binary Tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if data == 'null':
            return None
        data = data.split()
        
        def build():
            if not data:
                return None
            val = data.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val[1:]))
            node.left = build()
            node.right = build()
            return node
        
        return build()

# Example of an unbalanced tree
def create_unbalanced_tree():
    """
    Creates an unbalanced tree:
        1
       / \
      2   3
       \   \
        5   7
       /     \
      8       9
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)  # Creates imbalance on left
    root.left.right.left = TreeNode(8)  # Further imbalance
    root.right.right = TreeNode(7)  # Creates imbalance on right
    root.right.right.right = TreeNode(9)  # Further imbalance
    return root

# Example of a balanced tree
def create_balanced_tree():
    """
    Creates a balanced tree:
        1
       / \
      2   3
     / \ / \
    4  5 6  7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Test the trees
if __name__ == "__main__":
    # Create and test unbalanced tree

    unbalanced_root = create_unbalanced_tree()
    print('zigzag level order',unbalanced_root.zigzag_level_order(unbalanced_root))
    print("Unbalanced Tree Properties:")
    print("Height:", unbalanced_root.maxDepth(unbalanced_root))
    print("Is Balanced:", unbalanced_root.isBalanced(unbalanced_root))
    print('LCA of 8 and 9:', unbalanced_root.lowestCommonAncestor(unbalanced_root, unbalanced_root.left.right.left, unbalanced_root.right.right.right).value)
    
    # Create and test balanced tree
    balanced_root = create_balanced_tree()
    print("\nBalanced Tree Properties:")
    print("Height:", balanced_root.maxDepth(balanced_root))
    print("Is Balanced:", balanced_root.isBalanced(balanced_root))
    print('LCA of 4 and 5:', balanced_root.lowestCommonAncestor(balanced_root, balanced_root.left.left, balanced_root.left.right).value)