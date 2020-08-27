# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        this1 = l1
        this2 = l2
        if this1.val >= this2.val:
            first = this2
            this2 = this2.next
        else:
            first = this1
            this1 = this1.next
        this_node = first
        while (this1 is not None) or (this2 is not None):
            if this1 is None:
                this_node.next = this2
                this2 = this2.next
                this_node = this_node.next
            elif this2 is None:
                this_node.next = this1
                this1 = this1.next
                this_node = this_node.next
            elif this1.val >= this2.val:
                this_node.next = this2
                this2 = this2.next
                this_node = this_node.next
            elif this2.val >= this1.val:
                this_node.next = this1
                this1 = this1.next
                this_node = this_node.next
        return first

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

soln = Solution()
output = soln.mergeTwoLists(list1, list2)
while output is not None:
    print(output.val)
    output = output.next