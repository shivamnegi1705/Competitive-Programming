# Question Link:- https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        cur = l1
        while cur!=None:
            num1+=str(cur.val)
            cur = cur.next
        cur = l2
        while cur!=None:
            num2+=str(cur.val)
            cur = cur.next
        num1 = num1[-1::-1]
        num2 = num2[-1::-1]
        ans = str(int(num1)+int(num2))
        ans = ans[-1::-1]
        head = None
        cur = None
        i = 0
        while i<len(ans):
            if head==None:
                cur = ListNode(int(ans[i]))
                head = cur
            else:
                nex = ListNode(int(ans[i]))
                cur.next = nex
                cur = nex
            i+=1
        return head
