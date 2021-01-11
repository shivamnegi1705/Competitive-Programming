# Question Link:- https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ans = []
        cur = head
        while cur!=None:
            ans.append(cur.val)
            cur = cur.next
        ans[k-1],ans[-k] = ans[-k],ans[k-1]
        cur = head
        i = 0
        while cur!=None:
            cur.val = ans[i]
            i+=1
            cur = cur.next
        return head
