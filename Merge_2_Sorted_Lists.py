"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []

"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() # Create a dummy node
        l3 = dummy # Start from the dummy node
        while l1 and l2:
            if l1.val < l2.val: # If value of l1 is smaller
                l3.next = l1 # Add l1 to current l3
                l1 = l1.next # Move l1 to next
            else:
                l3.next = l2 # If value of l2 is smaller, add l2 to current l3
                l2 = l2.next # Move l2 to next
            l3 = l3.next # Move current to next
        l3.next = l1 or l2 # If one of the lists is exhausted, add the remaining list to current l3
        return dummy.next # Return the next node after the dummy node