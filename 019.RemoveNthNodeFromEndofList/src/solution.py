# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        # let fast go n steps before slow start, then when fast reach the end of list, 
        # slow would stay at the nth we need to remove counted from the end of list
        for _ in range(n):
            fast = fast.next
        if not fast: return head.next
        # one step further ensure the slow node could reach n + 1 from the end of the list
        fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head