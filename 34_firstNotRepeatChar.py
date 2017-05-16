# replace() 不改变当前字符串
class Solution():
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        index = 0
        for a in s:
            strCopy = s.replace(a, '')
            if len(strCopy) + 1 == len(s):
                return index
            index += 1


s = Solution()
result = s.FirstNotRepeatingChar("google")
print(result)
