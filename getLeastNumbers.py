class Solution():
    def getLeastNumber(self, tinput, k):
        if not tinput or k > len(tinput):
           return []
        tinput.sort()
        return tinput[:k]
a = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.getLeastNumber(a,10))
