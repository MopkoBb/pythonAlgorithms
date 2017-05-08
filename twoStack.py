class Solution:
    stack1 = list()
    stack2 = list()

    def push(self, node):
        # write code here
        if len(self.stack1) < 1:
            self.stack1.append(node)
        else:
            self.stack2.append(node)

    def pop(self):
        # return xx
        if self.stack1:
            result = self.stack1.pop()
            if self.stack1:
                return result
            else:
                if self.stack2:
                    while self.stack2:
                        self.stack1.append(self.stack2.pop())
                return result
        else:
            if self.stack2:
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
                if self.stack1 is not None:
                    return self.stack1.pop()

test = Solution()
test.push(1)
test.push(2)
test.push(3)
print(test.pop())
print(test.pop())
test.push(4)
print(test.pop())
test.push(5)
print(test.pop())
print(test.pop())