# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    prev=None
    while slow:
        temp=slow.next
        slow.next=prev
        prev=slow
        slow=temp
    left,right=head,prev
    while right:
        if left.val!=right.val:
            return False
        left=left.next
        right=right.next
    return True