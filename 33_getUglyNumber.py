# 需要注意给result一个确定大小的空间
# 丑数，从小到大排列，最新的数从以前的丑数中 *2 or *3 or *5 调最小
class Solution():
    def GetUglyNumber(self, index):
        if not index:
            return 0
        # 分配确定大小空间
        result = [1] * index
        t2, t3, t5 = 0, 0, 0
        nextIndex = 1
        while index-1:
            temp = min(result[t2]*2, result[t3]*3,result[t5]*5)
            result[nextIndex] = temp
            index -= 1
            nextIndex += 1
            if temp == result[t2]*2: t2 += 1
            if temp == result[t3]*3: t3 += 1
            if temp == result[t5]*5: t5 += 1
        return result

s = Solution()
a = s.GetUglyNumber(25)
print(a)
