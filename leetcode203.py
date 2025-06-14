# 203. Remove Linked List Elements
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head,val):
    newnode=ListNode(0)
    newnode.next=head
    curr=newnode
    while curr.next:
        if curr.next.val==val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return newnode.next

def removeElements(head,val):
    if head==None:
        return None
    while head!=None and head.val==val:
        head=head.next
    temp=head
    while temp and temp.next:
        if temp.next.val==val:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return head