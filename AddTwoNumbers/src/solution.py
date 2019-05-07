# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        acc1 = 0
        mu1 = 1
        acc2 = 0
        mu2 = 1
        while l1:
            acc1 += l1.val * mu1
            mu1 = mu1 * 10
            l1 = l1.next
        while l2:
            acc2 += l2.val * mu2
            mu2 = mu2 * 10
            l2 = l2.next
        rs = str(acc1 + acc2)
        print(rs)
        result = head = ListNode(0)
        for s in reversed(rs):
            head.next = ListNode(int(s))
            head = head.next
        return result.next
            