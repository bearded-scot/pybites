class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        pass

a = [[1, 2],  [3, 4]]
b = [[11, 12], [13, 14]]


x = [(a[0][0] * b[0][0]) + (a[0][1] * b[1][0]), (a[0][0] * b[0][1]) + (a[0][1] * b[1][1])]

y = [(a[1][0] * b[0][0]) + (a[1][1] * b[1][0]), (a[1][0] * b[0][1]) + (a[1][1] * b[1][1])]

a_ind = (0,0)
b_ind = (0,0)

