# 530. Minimum Absolute Difference in BST
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105

def getMinimumDifference(root):
        st=[]
        prev=float('-inf')
        mindiff=float('inf')
        while st or root:
            if root:
                st.append(root)
                root=root.left
            else:
                root=st.pop()
                mindiff=min(mindiff,root.val-prev)
                prev=root.val
                root=root.right
        return mindiff
        