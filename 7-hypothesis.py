import math
from typing import Tuple


def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0  # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0  # normal_cdf(10) is (very close to) 1
    mid_z = 0.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:  # midpoint is still too low, search above it
            low_z = mid_z
        else:  # midpoint is still too high, search below it
            hi_z = mid_z
    return mid_z


normal_prob_below = normal_cdf


def normal_prob_above(lo: float, mu: float = 0, sigma: float = 1) -> float:
    return 1 - normal_cdf(lo, mu, sigma)


def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    if x >= mu:
        return 2 * normal_prob_above(x, mu, sigma)
    else:
        return 2 * normal_prob_below(x, mu, sigma)


z = a_b_test(1000, 200, 500, 80)
p_value = two_sided_p_value(z)
print(z, p_value)

