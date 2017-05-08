class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        list = []
        while head:
            list.append(head.val)
            head = head.next
        return list[-k]

