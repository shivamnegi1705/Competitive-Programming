# Question Link:- https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        last = list2
        while last.next!=None:
            last = last.next
        cur = list1
        cnt = 0
        req = None
        while cur!=None:
            if cnt==b+1:
                req = cur
                break
            cur = cur.next
            cnt +=1
        cnt = 0
        cur = list1
        while cur!=None:
            if cnt==a-1:
                cur.next = list2
                break
            cnt+=1
            cur = cur.next
        last.next = req
        return list1
