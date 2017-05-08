class Solution():
    def judge(self, squence):
        root = squence[-1]
        cursor = 0
        for a in squence:
            if a < root:
                cursor += 1
        return self.judge(squence[0,cursor-1], squence[cursor, -2])
    def VerifySquenceOfBST(self, squence):
        if not squence:
            return False
        return judge(squence)
