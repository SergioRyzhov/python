class Matrix:
    def __init__(self, *args):
        self.matrix = []
        self.matrix_2 = []
        self.matrix_sum = []
        for i in args:
            self.matrix.append(i)

    def __str__(self):
        output = []
        for i in range(len(self.matrix)):
            output.append('\t' + '\t'.join([str(j) for j in self.matrix[i]]))
        return '\n'.join(output) + '\n\n'

    def __add__(self, other):
        """unparse other to int matrix"""
        temp_matr = format(other).strip().split('\n')
        tmp = []
        for i in range(len(temp_matr)):
            tmp.append(temp_matr[i].strip().split('\t'))
        for i in range(len(tmp)):
            self.matrix_2.append([int(j) for j in tmp[i]])

        temp_matr.clear()
        tmp.clear()

        """matrix addition"""
        if len(self.matrix_2) > len(self.matrix):
            height_mtrx = self.matrix_2.copy()
        else:
            height_mtrx = self.matrix.copy()

        if len(self.matrix_2[0]) > len(self.matrix[0]):
            width_mtrx = self.matrix_2.copy()
        else:
            width_mtrx = self.matrix.copy()

        for i in range(len(height_mtrx)):
            for j in range(len(width_mtrx[0])):
                try:
                    try:
                        try:
                            tmp.append(sum([self.matrix[i][j], self.matrix_2[i][j]]))
                        except IndexError:
                            tmp.append(sum([width_mtrx[i][j], 0]))
                    except IndexError:
                        tmp.append(sum([height_mtrx[i][j], 0]))
                except IndexError:
                    tmp.append(0)
            self.matrix_sum.append(tmp.copy())
            tmp.clear()
            output = []
        for i in range(len(self.matrix_sum)):
            output.append('\t' + '\t'.join([str(j) for j in self.matrix_sum[i]]))
        return '\n'.join(output) + '\n\n'


a = Matrix([31, 32], [37, 43], [51, 86])
b = Matrix([3, 5, 32], [2, 4, 6], [-1, 64, -8])
c = Matrix([3, 5, 8, 3], [8, 3, 7, 1])

print(a, b, c)
print('==================')
t = a + c
print(t)
