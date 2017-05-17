class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    # 使用长度
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        len1, len2 = 0, 0
        pCopy1, pCopy2 = pHead1, pHead2
        while pCopy1:
            len1 += 1
            pCopy1 = pCopy1.next
        pCopy1 = pHead1
        while pCopy2:
            len2 += 1
            pCopy2 = pCopy2.next
        pCopy2 = pHead2
        index = len1 - len2
        if index > 0:
            while index:
                pCopy1 = pCopy1.next
                index -= 1
        elif index < 0:
            while not index+1:
                pCopy2 = pCopy2.next
                index += 1
        while pCopy1.val != pCopy2.val:
            pCopy1 = pCopy1.next
            pCopy2 = pCopy2.next
        return pCopy1

    # 假定 List1长度: a+n  List2 长度:b+n, 且 a<b 
    # 那么 p1 会先到链表尾部, 这时p2 走到 a+n位置,将p1换成List2头部
    # 接着p2 再走b+n-(n+a) =b-a步到链表尾部,这时p1也走到List2的b-a位置，还差a步就到可能的第一个公共节点。
    # 将p2换成List1头部，p2走a步也到可能的第一个公共节点。
    # 如果恰好p1==p2,那么p1就是第一个公共节点。 或者p1和p2一起走n步到达列表尾部，二者没有公共节点，退出循环。 同理a>=b.
    # 时间复杂度O(n+a+b)
    def FindFirstCommonNode2(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        pCopy1, pCopy2 = pHead1, pHead2
        while pCopy1.val != pCopy2.val:
            pCopy1 = pCopy1.next
            pCopy2 = pCopy2.next
            if pCopy1.val != pCopy2:
                if pCopy1 == None: pCopy1 = pHead2
                if pCopy2 == None: pCopy2 = pHead1
        return pCopy1

