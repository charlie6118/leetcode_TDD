# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA = headA
        hB = headB
        lenA = 0
        lenB = 0
        while headA:
            lenA += 1
            headA = headA.next
        while headB:
            lenB += 1
            headB = headB.next
        for i in range(lenA - lenB):
            hA = hA.next
        for i in range(lenB - lenA):
            hB = hB.next
            
        while hA != hB:
            hA = hA.next
            hB = hB.next
        return hA