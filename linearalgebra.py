# Chapter 4
from typing import List, Tuple, Callable

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "No vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different sizes!"
    return [sum(v[i] for v in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def distance(v: Vector, w: Vector) -> float:
    return sum([(v_i - w_i) ** 2 for v_i, w_i in zip(v, w)])


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


Matrix = List[List[float]]


def shape(a: Matrix) -> Tuple[int, int]:
    num_rows = len(a)
    num_cols = len(a[0]) if a else 0  # number of elements in first row
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


