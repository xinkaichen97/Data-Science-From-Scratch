import math
from collections import Counter


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_v[mid] + sorted_v[mid - 1]) / 2
    else:
        return sorted_v[mid]


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print(quantile([2, 4, 8, 16, 32], 0.3))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


print(mode([1, 2, 2, 5, 5, 5, 6]))


# From 4-vectors.py
def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v):
    return dot(v, v)


def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    # return sum_of_squares(deviations) / (n - 1)
    return sum([v_i * v_i for v_i in deviations]) / (n - 1)


def stddev(x):
    return math.sqrt(variance(x))


print(variance([1, 2]))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stddev_x = stddev(x)
    stddev_y = stddev(y)
    if stddev_x > 0 and stddev_y > 0:
        return covariance(x, y) / stddev_x / stddev_y
    else:
        return 0