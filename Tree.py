#%%
"""
Topics / Patterns in Trees:
1. Traversals
    a. Inorder Traversal
    b. Preorder Traversal
    c. Postorder Traversal
    d. Levelorder Traversal
2. Node Count and Sum
    a. Count Nodes
    b. Sum of Nodes
3. Value Queries
    a. Maximum Value
    b. kth Level Sum
4. Tree Properties
    a. Height of Binary Tree
    b. Diameter of Binary Tree
    c. Maximum Depth of Binary Tree
    d. Minimum Depth of Binary Tree
5. Tree Symmetry and Equality
    a. Symmetric Tree
    b. Same Tree
6. Subtree Queries
    a. Subtree of Another Tree
7. Serialization and Deserialization
    a. Serialize and Deserialize Binary Tree (DFS)
    b. Serialize and Deserialize Binary Tree (BFS)
8. Additional Topics (To be done)
    a. Lowest Common Ancestor
    b. Path Sum Problems
    c. Balanced Binary Tree Check
    d. Binary Search Tree (BST) Operations
    e. AVL Tree and Red-Black Tree (Self-Balancing Trees)
"""
"""
1. Tree Traversals
Pattern Name: Traversal Techniques
Sub-parts:
a. Inorder Traversal (Recursive & Iterative)
b. Preorder Traversal (Recursive & Iterative)
c. Postorder Traversal (Recursive & Iterative)
d. Level Order Traversal (BFS)
e. Spiral/Zigzag Traversal
f. Boundary Traversal
g. Diagonal Traversal
h. Vertical Order Traversal
i. Morris Traversal (Inorder/Preorder without recursion or stack)
2. Construction of Trees
Pattern Name: Tree Construction
Sub-parts:
a. Construct Binary Tree from Inorder and Preorder Traversal
b. Construct Binary Tree from Inorder and Postorder Traversal
c. Construct Binary Tree from Level Order and Inorder Traversal
d. Construct BST from Preorder Traversal
e. Construct BST from Postorder Traversal
f. Construct BST from Level Order Traversal
g. Construct Full Binary Tree from Preorder and Postorder Traversal
h. Construct Binary Tree from Parent Array Representation
i. Construct Binary Tree from String Representation
3. Binary Search Tree (BST)
Pattern Name: BST Operations
Sub-parts:
a. Search in a BST
b. Insert into a BST
c. Delete a Node in a BST
d. Find Minimum/Maximum in a BST
e. Check if a Tree is a Valid BST
f. Inorder Successor/Predecessor in BST
g. Convert Sorted Array to Balanced BST
h. Convert BST to Balanced BST
i. Merge Two BSTs
j. Kth Smallest/Largest Element in BST
k. Largest BST in a Binary Tree
4. Tree Properties
Pattern Name: Tree Properties
Sub-parts:
a. Height/Depth of a Tree
b. Diameter of a Tree
c. Check if a Tree is Balanced
d. Check if Two Trees are Identical
e. Check if a Tree is Symmetric
f. Check if a Tree is a Subtree of Another Tree
g. Check if a Tree is a Complete Binary Tree
h. Check if a Tree is a Full Binary Tree
i. Check if a Tree is a Perfect Binary Tree
j. Count the Number of Nodes in a Tree
k. Count Leaf Nodes in a Tree
l. Maximum/Minimum Element in a Tree
m. Sum of All Nodes in a Tree
5. Path Problems
Pattern Name: Path-Based Problems
Sub-parts:
a. Root to Leaf Path Sum
b. Maximum Path Sum in a Binary Tree
c. Longest Path in a Binary Tree (Diameter)
d. Print All Root-to-Leaf Paths
e. Check if a Path Exists with a Given Sum
f. Lowest Common Ancestor (LCA) in a Binary Tree
g. LCA in a BST
h. Shortest Path Between Two Nodes in a Tree
i. Maximum Sum Path Between Two Leaves
6. Tree Views
Pattern Name: Tree Views
Sub-parts:
a. Left View of a Binary Tree
b. Right View of a Binary Tree
c. Top View of a Binary Tree
d. Bottom View of a Binary Tree
e. Diagonal View of a Binary Tree
"""
# TreeNode class and methods
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Inorder Traversal - DFS-Recursive Approach
    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)
        return result
    # Preorder Traversal - DFS-Recursive Approach
    def preorder_traversal(self, root, result):
        if root:
            result.append(root.value)
            self.preorder_traversal(root.left, result)
            self.preorder_traversal(root.right, result)
        return result
    # Postorder Traversal - DFS-Recursive Approach
    def postorder_traversal(self, root, result):
        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.value)
        return result
    # Levelorder Traversal - BFS-Iterative Approach
    # Level order traversal is a tree traversal algorithm that 
    # visits all the nodes of a tree level by level.
    """Big O Notation: O(n)
    Memory Complexity: O(n)"""
    def levelorder_traversal(self, root):
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
    #Count Nodes - DFS-Recursive Approach
    #Given a binary tree, count the number of nodes in the tree.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    # Sum of Nodes - DFS-Recursive Approach
    # Given a binary tree, find the sum of all nodes in the tree.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def sumNodes(self, root):
        if not root:
            return 0
        return root.value + self.sumNodes(root.left) + self.sumNodes(root.right)
    # Maximum Value - DFS-Recursive Approach
    # Given a binary tree, find the maximum value in the tree.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def maxValue(self, root):
        if not root:
            return float('-inf')
        return max(root.value, self.maxValue(root.left), self.maxValue(root.right))
    #Height of Binary Tree - DFS-Recursive Approach
    #The height of a binary tree is the number of edges
    #on the longest path between the root node and a leaf node.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))     
    # Diameter of Binary Tree - DFS-Recursive Approach
    # The diameter of a binary tree is the length of the longest path
    # between any two nodes in a tree. This path may or may not pass
    #  through the root.
    """Big O Notation: O(n^2),Memory Complexity: O(n)"""
    def diameterOfBinaryTree1(self, root):
        def height(root):
            if not root:
                return -1
            return 1 + max(height(root.left), height(root.right))

        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        left_diameter = self.diameterOfBinaryTree1(root.left)
        right_diameter = self.diameterOfBinaryTree1(root.right)

        return max(left_height + right_height + 2, left_diameter, right_diameter)
    #Approach 2: Diameter of Binary Tree - DFS-Recursive Approach
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def diameterOfBinaryTree(self, root):
        self.diameter = 0#global variable
        def height(root):
            if not root:
                return -1
            left_height = height(root.left)
            right_height = height(root.right)
            self.diameter = max(self.diameter, left_height + right_height + 2)
            return 1 + max(left_height, right_height)
        height(root)
        return self.diameter


    # Maximum Depth of Binary Tree - DFS-Recursive Approach
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    # Minimum Depth of Binary Tree - DFS-Recursive Approach
    # The minimum depth is the number of nodes along the 
    # shortest path from the root node down to the nearest leaf node.
    # Note: A leaf is a node with no children.
    #ie. if a node has only one child, 
    #then the depth of the tree is the depth of that child.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    # Symmetric Tree - DFS-Recursive Approach
    # A binary tree is symmetric if the left subtree is a mirror
    # reflection of the right subtree.
    # Note: This is not the same as a binary tree 
    # being a mirror image of itself.
    # The left and right subtrees must be mirror images of each other.
    """Big O Notation: O(n),Memory Complexity: O(n)"""
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.value == right.value) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root, root)
    # Same Tree - DFS-Recursive Approach
    # Given two binary trees, write a function to check if they are the same or not.
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.value == q.value and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #Subtree of Another Tree - DFS-Recursive Approach
    #Given two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    # 2 cycles Recursive Approach-
    """
    Approach	Time Complexity	Space Complexity
    Brute Force (Recursive Comparison)	O(N × M)	O(H) (call stack)
    Case	Space Complexity
    Balanced Tree (H = O(log N))	O(log N)
    Skewed Tree (H = O(N))	O(N)
    """
    """Big O Notation: O(n*m),Memory Complexity: O(n) if the tree is skewed, O(log n) if the tree is balanced"""
    def isSubtree(self,root,subRoot):
        if not root and not subRoot:
            return True
        # if not root or not subRoot: # redundant
        #     return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    #Optimized (Serialization + Substring Search)	O(N + M)	O(N + M)
    """Big O Notation: O(n+m),Memory Complexity: O(n+m)"""
    #Serialize the tree and then check if the subRoot is in the root
    
    def isSubtree(self, root, subRoot):
        def serialize(root):
            if not root:
                return 'null'
            return f'#{root.value} {serialize(root.left)} {serialize(root.right)}'
        
        return serialize(subRoot) in serialize(root)
    #Optimized (Preorder Traversal + String Conversion)	O(N + M)	O(N + M)
    def isSubtree(self, root, subRoot): 
        def convert(p):
            return f'#{p.value} {convert(p.left)} {convert(p.right)}' if p else 'null'
        return convert(subRoot) in convert(root)
    #kth level sum
    def kthLevelSum(self, root, k):
        if not root:
            return 0
        if k == 0:
            return root.value
        return self.kthLevelSum(root.left, k - 1) + self.kthLevelSum(root.right, k - 1)
    #kth level sum
    def kthLevelSum(self, root, k):
        queue = [(root, 0)]
        result = 0
        while queue:
            node, level = queue.pop(0)
            if level == k:
                result += node.value
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result
    #kth level sum
    ""
    def kthLevelSum(self, root, k):
        queue = [root]
        level = 0
        while queue:
            level += 1
            if level == k:
                return sum(node.value for node in queue)
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return 0
    # Topic: Serialize and Deserialize Binary Tree
    # Serialize : Convert a binary tree to a string representation.
    # Deserialize : Convert a string representation to a binary tree.
    #Serialize and Deserialize Binary Tree - DFS-Recursive Approach
    #Preorder Traversal Approach -root,left,right
    def serialize(self, root):
        if not root:
            return 'null'
        return f'#{root.value} {self.serialize(root.left)} {self.serialize(root.right)}'
    def deserialize(self, data):
        if data == 'null':
            return None
        data = data.split()
        #break
        def b(data):

            if not  data:
                return None 
            n=data.pop(0)
            if n=='null':
                return None
            node=TreeNode(int(n[1:]))
            node.left=b(data)
            node.right=b(data)
            return node

        #break #breakpoint
        return b(data)
            
        
    #Serialize and Deserialize Binary Tree - BFS-Iterative Approach
    #Level Order Traversal Approach
    def serialize_bfs(self, root):
        if not root:
            return 'null'
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.value))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        return ','.join(result)
    def deserialize_bfs(self, data):
        if data == 'null':
            return None
        data = data.split(',')
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            left = data.pop(0)
            right = data.pop(0)
            if left != 'null':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != 'null':
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root


#%%

print("si", root.seliz(root))
            
# Demo
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(10)

#%%_
print("Inorder Traversal:", root.inorder_traversal(root, []))
print("Preorder Traversal:", root.preorder_traversal(root, []))
print("Postorder Traversal:", root.postorder_traversal(root, []))
print("Levelorder Traversal:", root.levelorder_traversal(root))
print("Count Nodes:", root.countNodes(root))
print("Sum of Nodes:", root.sumNodes(root))
print("Maximum Value:", root.maxValue(root))
print("Height of Binary Tree:", root.height(root))
print("Diameter of Binary Tree:", root.diameterOfBinaryTree1(root))
print("Diameter of Binary Tree:", root.diameterOfBinaryTree(root))
print("Maximum Depth of Binary Tree:", root.maxDepth(root))
print("Minimum Depth of Binary Tree:", root.minDepth(root))
print("Symmetric Tree:", root.isSymmetric(root))
print("Same Tree:", root.isSameTree(root, root))
#%%
print("Subtree of Another Tree:", root.isSubtree(root, root.left))
print("Subtree of Another Tree:", root.isSubtree(root, root.right))
print("Subtree of Another Tree:", root.isSubtree(root, root.left.left))
print("Subtree of Another Tree:", root.isSubtree(root, root.left.right))
print("Subtree of Another Tree:", root.isSubtree(root, root.right.left))
#%%
print("kth Level Sum:", root.kthLevelSum(root, 2))
#%%
print("Serialize:", root.serialize(root))
print("Deserialize:", root.deserialize(root.serialize(root)))
#%%
#deserialize Graph drawing
def draw_tree(root, ax, x, y, dx, dy):
    if root:
        # Draw the current node
        ax.add_artist(plt.Circle((x, y), 0.05, color='lightblue'))
        ax.text(x, y, str(root.value), ha='center', va='center', fontsize=12, color='black')
        
        # Draw left subtree
        if root.left:
            ax.add_artist(plt.Line2D((x, x - dx), (y, y - dy), color='black'))
            draw_tree(root.left, ax, x - dx, y - dy, dx / 2, dy)
        
        # Draw right subtree
        if root.right:
            ax.add_artist(plt.Line2D((x, x + dx), (y, y - dy), color='black'))
            draw_tree(root.right, ax, x + dx, y - dy, dx / 2, dy)
deserialized_root = root.deserialize(root.serialize(root))
draw_tree(deserialized_root, ax, 0, 0, 0.5, 0.2)
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Draw the tree
draw_tree(root, ax, 0, 0, 0.5, 0.2)

# Show the plot
plt.show()

#%%
print(root.seliz(root))


#%%
root
# Draw Tree using Matplotlib

import matplotlib.pyplot as plt

def draw_tree(root, ax, x, y, dx, dy):
    if root:
        # Draw the current node
        ax.add_artist(plt.Circle((x, y), 0.05, color='lightblue'))
        ax.text(x, y, str(root.value), ha='center', va='center', fontsize=12, color='black')
        
        # Draw left subtree
        if root.left:
            ax.add_artist(plt.Line2D((x, x - dx), (y, y - dy), color='black'))
            draw_tree(root.left, ax, x - dx, y - dy, dx / 2, dy)
        
        # Draw right subtree
        if root.right:
            ax.add_artist(plt.Line2D((x, x + dx), (y, y - dy), color='black'))
            draw_tree(root.right, ax, x + dx, y - dy, dx / 2, dy)


# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Draw the tree
draw_tree(root, ax, 0, 0, 0.5, 0.2)

# Show the plot
plt.show()
# explain how to draw the tree
#position of the root node is (0,0)
#position of the left child is (-0.5,-0.2)
#position of the right child is (0.5,-0.2)
#position of the left child of the left child is (-0.75,-0.4)