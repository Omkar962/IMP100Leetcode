# 1382. Balance a Binary Search Tree
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

# Example 1:


# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105


def balanceBST(self, root):
    nodes = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        nodes.append(node)
        inorder(node.right)

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
