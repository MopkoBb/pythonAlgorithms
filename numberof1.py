class Solution:
    def NumberOf1(self, n):
        # real = []
        # num = 0
        # if n == 0:
        #     return 0
        # if n > 0:
        #     binary = list(bin(n))[2:]
        # else:
        #     binary = list(bin(n))[3:]
        #     for a in binary:
        #         if a == '1':
        #             real.append('0')
        #         else:
        #             real.append('1')
        #     jinwei = 0
        #     c = int(real.pop()) + 1
        #     result = []
        #     if c == 2:
        #         jinwei = 1
        #         result.append('0')
        #     else:
        #         jinwei = 0
        #         result.append('1')
        #     while real:
        #         if jinwei:
        #             c = int(real.pop()) + jinwei
        #             if c == 2:
        #                 jinwei = 1
        #                 result.append('0')
        #             else:
        #                 jinwei = 0
        #                 result.append('1')
        #         else:
        #             result.append(real.pop())
        #     binary = result[::-1]
        # print(binary)
        # for item in binary:
        #     if item == '1':
        #         num += 1
        # return num

        count = 0
        if n < 0:
            n = n & 0x7FFFFFFF
            count += 1
        while n:
            count += 1
            n = n & (n-1)
        return count

print(Solution().NumberOf1(-1))

