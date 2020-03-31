from collections import Counter
from collections import defaultdict
import random
from functools import partial
import re


def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)


print(apply_to_one(lambda x: x + 4))

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

x = [4, 1, 2, 3]
y = sorted(x)  # is [1,2,3,4], x is unchanged
x.sort()

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)
z = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.randrange(3, 6))
print(random.shuffle(z))

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)


class Set:

    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([1,2,3])
s.add(4)
print(s.contains(4)) # True
s.remove(3)
print(s.contains(3))


def exp(base, power):
    return base ** power


two_to_the = partial(exp, 2) # is now a function of one variable
print(two_to_the(3))


def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
for i in lazy_evens_below_20:
    print(i, end=' ')
print()

print(all([not re.match("a", "cat"), re.search("a", "cat"), not re.search("c", "dog"),
           3 == len(re.split("[ab]", "carbs")), "R-D-" == re.sub("[0-9]", "-", "R2D2")]))

documents = ['a', 'b', 'c']
for i, document in enumerate(documents):
    print(i, document)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipresults = zip(list1, list2)
print(zipresults, list(zipresults))
print(list(zip(('a', 1), ('b', 2), ('c', 3))))
print(list(zip(*[('a', 1), ('b', 2), ('c', 3)])))


def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, 5, key="word", key2="word2", key3="word3")


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = { "z" : 3 }
print(other_way_magic(*x_y_list, **z_dict))
