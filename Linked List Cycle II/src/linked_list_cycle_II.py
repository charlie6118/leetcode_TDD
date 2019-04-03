# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print(head.val)
        if head.val == None:
            return head
        if head.next == None:
            return None
        head.val = None
        return self.detectCycle(head.next)
 
head = ListNode(3)
snd = ListNode(2)
thrid = ListNode(0)
fourth = ListNode(-4)

head.next = snd
snd.next = thrid
thrid.next = fourth
fourth.next = snd

S = Solution()

print(S.detectCycle(head))