# 重写cmp函数
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        stack = [str(a) for a in numbers]
        stack.sort(cmp=self.cmp)
        return ''.join(stack)

    def cmp(self, n1, n2):
        print(n1, n2)
        s1 = n1 + n2
        s2 = n2 + n1
        print(s1, s2)
        print('******')
        if s1 > s2:
            return 1
        else: return -1

s = Solution()
nums = [3, 32, 321]
result = s.PrintMinNumber(nums)
print(result)
