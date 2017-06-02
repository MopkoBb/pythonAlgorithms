# -*- coding:utf-8 -*-
class Solution():
    def duplicate(self, numbers, duplication):
        if not numbers:
            return 0
        temp = []
        for a in numbers:
            temp.append(a)
        print(temp)
        length = len(numbers)
        for a in numbers:
            temp.remove(a)
            print(length - len(temp))
            if length - len(temp) > 1:
                duplication[0] = a
                return True
            temp.append(a)

s = Solution()
print(s.duplicate([1,2,1,3,4], []))