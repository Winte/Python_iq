"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     prev = None # previous node, initially None.
     curr = head # current node, initially the head of the linked list
    
     while curr: # We iterate over the linked list then we reverse the next pointer
        nxt = curr.next 
        curr.next = prev
        prev = curr
        curr = nxt
    
     return prev