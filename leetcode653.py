# 653. Two Sum IV - Input is a BST
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

def findTarget(root,k):
    seen=set()
    def dfs(node):
        if not node:
            return False
        if (k-node.val) in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)