# Question Link:- https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        cur = l1
        while cur!=None:
            arr.append(cur.val)
            cur = cur.next
        cur = l2
        while cur!=None:
            arr.append(cur.val)
            cur = cur.next
        if arr==[]:
            return None
        arr.sort()
        head = ListNode(arr[0])
        cur = head
        for i in arr[1::]:
            nex = ListNode(i)
            cur.next = nex
            cur = nex
        return head
