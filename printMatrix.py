class Solutoin():

    def printMatrix(self, matrix):
        # if matrix:
        #     print('aaaa')
        #     return False
        result = []
        while matrix:
            for a in matrix[0]:
               result.append(a)
            matrix.pop(0)
            if matrix:
                for i in range(len(matrix)):
                    if matrix[i]:
                        result.append(matrix[i].pop())

            if matrix:
                while matrix[-1]:
                    result.append(matrix[-1].pop())
                matrix.pop()
            if matrix:
                for i in range(len(matrix)-1,0,-1):
                    if matrix[i]:
                        result.append(matrix[i].pop(0))
        return result
a = Solutoin()
# print(a.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
# print(a.printMatrix([[1]]))
print(a.printMatrix([[1],[2],[3],[4],[5]]))