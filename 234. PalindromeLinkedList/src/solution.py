# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # get middle point
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # push the second part into stack
        s = []
        while slow:
            s.append(slow.val)
            slow = slow.next
        print(s)
        
        # pop and compare
        while s:
            if s.pop() != head.val:
                return False
            head = head.next
        return True