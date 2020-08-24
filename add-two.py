# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        start_node = ListNode((l1.val + l2.val)%10)
        this_node = start_node
        carried = (l1.val + l2.val) // 10
        while l1.next is not None or l2.next is not None or carried != 0:
            if l1.next is not None:
                l1 = l1.next
                carried += l1.val
            if l2.next is not None:
                l2 = l2.next
                carried += l2.val
            new_node = ListNode(carried % 10)
            carried = carried // 10
            this_node.next = new_node
            this_node = new_node
        return start_node

# 72-88 ms runtime, 13.7-14.1 MB memory use per leetcode