import random
from typing import List, Optional, Callable

first_name = "Xinkai"
last_name = "Chen"
full_name = f"{last_name.upper()}, {first_name}"
print(full_name)

assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"


class CountingClicker:

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker = CountingClicker(100)
assert clicker.read() == 100
clicker.click(50)
clicker.click(50)
assert clicker.read() == 200
clicker.reset()
assert clicker.read() == 0


class NoResetClicker(CountingClicker):

    def reset(self):
        pass


clicker2 = NoResetClicker(100)
assert clicker2.read() == 100
clicker2.click(50)
assert clicker2.read() == 150
clicker.reset()
assert clicker2.read() == 150

up_to_five = [1, 2, 3, 4, 5]
random.shuffle(up_to_five)
print(up_to_five)


def total(xs: List[float]) -> float:
    return sum(xs)


print(total([1.0, 3.0, 5.0]))

values: List[int] = []
best_so_far: Optional[float] = None


def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)
