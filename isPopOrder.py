class Solution():
    def isPopOrder(self, pushA, popB):
        realPop = []
        while pushA:
            realPop.append(pushA.pop())
        if realPop == popB:
            return True
