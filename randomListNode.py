class RandomListNode():
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution():
    # 递归
    def Clone(self, pHead):
        if not pHead:
            return None
        pCloneNode = RandomListNode(pHead.label)
        pCloneNode.random = pHead.random
        pCloneNode.next = self.Clone(pHead.next)
        return pCloneNode

    # 三步法
    def Clone1(self, pHead):
        pNode = pHead
        while pNode:
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random:
                pClone.random = pNode.random.next
            pNode = pClone.next

        pNode = pHead
        pCloneHead = pNode.next
        while pNode:
            tmp = pNode.next
            if tmp:
                pNode.next = tmp.next
            pNode = tmp
        return pCloneHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone1(node1)
while clonedNode:
    print(clonedNode.label)
    if clonedNode.random:
        print('->')
        print(clonedNode.random.label)
    clonedNode = clonedNode.next
