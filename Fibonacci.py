class Solution:
    def Fibonacci(self, n):
        # # write code here
        # x = 1
        # pre = 1
        # dpre = 1
        # num = 0
        # while num < n:
        #     if num < 2:
        #         x = 1
        #     else:
        #         x = dpre + pre
        #         dpre = pre
        #         pre = x
        #     num += 1
        # return x
        if n < 1: return 0
        if n < 2: return 1
        return self.Fibonacci(n-2) + self.Fibonacci(n-1)

so = Solution()
print(so.Fibonacci(4))