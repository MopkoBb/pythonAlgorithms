# -*- coding:utf-8 -*-
class Solution():
    def LastRemaining_Solution(self, n, m):
        children = [1] * n
        count, step, i = n, 0, 0
        while count > 0:
            i += 1
            if i == n:
                i = 0
            if children[i] == -1:
                continue
            step += 1
            if step == m-1:
                children[i] = -1
                step = -1
                count -= 1
        return i

    # 分析法 通过分析得出映射函数有 P(x) = (x-k-1)%n -> P-1(x) = (x+k+1)%n
    # f(n,m) = f`(n-1,m) = P(f(n)) = [f(n-1,m)+m]%n n>1
    def LastRemaining_Solution2(self, n, m):
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        else:
            return (self.LastRemaining_Solution2(n-1, m) + m) % n

    # 使用循环效率高很多
    def LastRemaining_Solution3(self, n, m):
        if n < 1:
            return -1
        flag, result = 2, 0
        while flag <= n:
            result = (result + m) % flag
            flag += 1
        return result
s = Solution()
a = s.LastRemaining_Solution3(4000, 997)
print(a)
