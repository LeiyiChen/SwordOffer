# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return head
        h = head
        res = []
        while h:
            res.append(h)
            h = h.next
        if k > len(res) or k <=0:
            return None
        return res[-k]
        # second solution
        '''
        if head is None or k <= 0:
            return None
        p = q = head
        i = k - 1
        while i > 0 and p:
            p = p.next
            i -= 1
        if p is None:
            return None
        while p.next:
            p = p.next
            q = q.next
        return q

        '''