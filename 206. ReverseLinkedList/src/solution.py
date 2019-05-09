# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rec(self, curr, newPre):
        if not curr:
            return newPre
        newCurr = curr.next
        curr.next = newPre
        return self.rec(newCurr, curr)
    
    def recReverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.rec(head, None)
        
    def iteReverseList(self, head):
        pre = None
        while head:
            newHead = head.next
            head.next = pre
            pre = head
            head = newHead
        return pre