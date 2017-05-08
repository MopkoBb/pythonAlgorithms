class Solution:
    def reOrderArray(self, array):
        pre = []
        end = []
        for a in array:
            if a % 2 == 0:
                end.append(a)
            else:
                pre.append(a)
        result = []
        result.extend(pre)
        result.extend(end)
        return result

so = Solution()
print so.reOrderArray([1,2,3,4,5,6,7])
