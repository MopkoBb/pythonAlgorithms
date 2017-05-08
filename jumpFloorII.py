class Solution:
    def jumpFloorII(self, number):
        # write code here
        # preSum = 3
        # num = 3
        # x = 4
        # if number < 3:
        #     return number
        # if number < 4:
        #     return number + 1
        # while num < number:
        #     x = x + preSum
        #     result = x + 1
        #     preSum = x
        #     num += 1
        # return result
        num = 1
        result = 1
        if number < 2:
            return number
        while num < number:
            result *= 2
            num += 1
        return result

so = Solution()
print(so.jumpFloorII(0))