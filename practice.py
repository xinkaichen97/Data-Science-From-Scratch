from functools import reduce


def greater_than_five(number):
    if number > 5:
        return number
    else:
        pass


numbers = range(1, 10)

judgement = list(map(lambda x: x > 5, numbers))
print(judgement)

result = list(filter(lambda x: x > 5, numbers))
print(result)

product = reduce((lambda x, y: x * y), numbers)
print(product)
