from functools import reduce, partial
import math


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


"""
def vector_sum(vectors):
    result = vectors[0]
    for v in vectors[1:]:
        result = vector_add(result, v)
    return result
"""


def vector_sum(vectors):
    return reduce(vector_add, vectors)


print(vector_add([1, 2, 3], [3, 4, 5]))
print(vector_subtract([4, 6], [5, 1]))
vectors = [[1, 2, 4], [3, 5, 8]]
print(vector_sum(vectors))
vector_sum = partial(reduce, vector_add)
print(vector_sum(vectors))


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


print(dot([1, 4], [2, 3]))


def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


print(magnitude([3, 4]))


def distance(v, w):
    return magnitude(vector_subtract(v, w))


print(distance([0, 0], [3, 4]))

# -------------- Matrix -------------
print('-------------- Matrix -------------')

A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]
B = [[1, 2],  # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols


def get_row(A, i):
    return A[i] # A[i] is already the ith row


def get_column(A, j):
    return [A_i[j] for A_i in A]


print(shape(A))
print(get_row(A, 1))
print(get_column(A, 2))


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


print(make_matrix(5, 5, is_diagonal))

