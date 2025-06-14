# 226. Invert Binary Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root):
    if not root:
        return None
    st=[root]
    while st:
        node=st.pop()
        node.left,node.right=node.right,node.left
        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)
    return root