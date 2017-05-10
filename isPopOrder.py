# 创建备用栈stack, 储存没有提前出栈的元素
# 在第一循环
# 1、如果pushV[0] == popV[0]，将两个出栈，continue
# 2、否则将pushV[0]压入stack
# 跳出循环， 期待的结果应该是stack == popV[::-1]

class Solution():
    def isPopOrder(self, pushV, popV):
        if not pushV or not popV:
            return False
        if len(pushV) == 1 and len(popV) == 1 and pushV == popV:
            return True
        stack = []
        while pushV:
            if pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
                continue
            else:
                stack.append(pushV.pop(0))
        if stack == popV[::-1]:
            return True
        else: return False
