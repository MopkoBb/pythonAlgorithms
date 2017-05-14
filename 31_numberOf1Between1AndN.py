class Solutoin():
    def numberOf1(self, n):
        number = 0
        for a in list(str(n)):
            if a == '1':
                number += 1
        return number
    def NumberOf1Between1AndN(self, n):
        number = 0
        for a in range(1,n+1):
            number += self.numberOf1(a)
        return number

    # the leetcode answer
    def answer(self, n):
        m, number = 1, 0
        while m < n:
            number += (n/m+8) / 10 * m + ((n/m) % 10 == 1) * (n%m+1)
            m *= 10
        return number

s = Solutoin()
a = s.NumberOf1Between1AndN(13)
print(a)
