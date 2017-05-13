# 出现的次数超过一半，则列表排序后，最中间的那个数一定是出现次数最多的
class Solution():
    def MoreThanHalfNum(self, numbers):
        if not numbers:
            return numbers
        numbers.sort()
        mid = numbers[int(len(numbers)/2)+1]
        num = 0
        for a in numbers:
            if a == mid:
                num += 1
        if num <= len(numbers)/2:
            return 0
        else:
            return numbers[int(len(numbers)/2)]

numbers = [1,2,3,2,2,2,5,4,2]
s = Solution()
a = s.MoreThanHalfNum(numbers)
print(a)
