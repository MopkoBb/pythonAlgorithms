class Solution():
    def reverseList(head):
        if not head:
            return None
        node = head
        head = head.next
        node.next = None
        while head:
            preNode = node
            node = head
            head = head.next
            node.next =preNode
        return node
