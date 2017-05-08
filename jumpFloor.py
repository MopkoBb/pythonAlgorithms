class Solution:
    def jumpFloor(self, number):

        x = 1
        pre = 1
        dpre = 0
        num = 0
        while num < number:
            x = dpre + pre
            dpre = pre
            pre = x
            num += 1
        return x
print(Solution().jumpFloor(3))