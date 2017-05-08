class Solution:
    # 非递归版本
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        pNode1 = pHead1
        pNode2 = pHead2
        if pNode1.val <= pNode2.val:
            merge = pNode1
            pNode1 = pNode1.next
        else:
            merge = pNode2
            pNode2 = pNode2.next

        pHead = merge
        while pNode1 or pNode2:
            if not pNode1:
                merge.next = pNode2
                pNode2 = pNode2.next
            elif not pNode2:
                merge.next = pNode1
                pNode1 = pNode1.next
            else:
                 if pNode1.val <= pNode2.val:
                     merge.next = pNode1
                     pNode1 = pNode1.next
                 else:
                     merge.next = pNode2
                     pNode2 = pNode2.next
            merge = merge.next
        return pHead
    def MergeII(self, pHead1, pHead2):
        # 递归版本
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.MergeII(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.MergeII(pHead1, pHead2.next)
            return pHead2




