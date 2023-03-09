print('----1.1----')


def my_map(func, iterable):
    for item in iterable:
        yield func(item)


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

for num in squared_numbers:
    print(num)

print('----1.2----')


def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('my_reduce() of empty sequence with no initial value')
    res = initializer
    for item in it:
        res = func(res, item)
        yield res


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)

print(list(result)[-1])

print('----1.3----')


def my_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step


result = my_range(1, 10, 2)

for num in result:
    print(num)

print('----2----')


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 2
        return value


my_iterable = MyIterable([1, 2, 3, 4, 5])
for value in my_iterable:
    print(value)


print("----3----")

my_list = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

for val in my_iter:
    print(val)