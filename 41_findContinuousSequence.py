# -*- coding:utf-8 -*-
class Solution():
    def FindContinuousSquence(self, tsum):
        if tsum < 3:
            return []
        result = []
        mid = (tsum + 1) / 2
        start, end = 1, 2
        rSum = start + end
        while start < mid:
            if rSum == tsum:
                result.append(range(start, end+1))
                start += 2
                end += 1
                print(start*2-3)
                rSum -= start * 2 - 3
                print(start, end, rSum)
                rSum += end
            elif rSum < tsum:
                end += 1
                rSum += end
            else:
                rSum -= start
                start += 1
        return result

s = Solution()
a = s.FindContinuousSquence(100)
print(a)