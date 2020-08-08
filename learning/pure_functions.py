from functools import reduce

# map
num_set = {1, 1, 2, 2, 3, 3, 4, 1}


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, num_set)))
print(num_set)

# filter
num_set_filter = {1, 3, 2, 3, 4, 5, 6, 7, 8, 9}


def isOdd(item):
    return item % 2 != 0


print(list(filter(isOdd, num_set_filter)))

# filter example 2
name_set = [
    {"name": "rob", "age": 4},
    {"name": "mat", "age": 2},
    {"name": "arron"}
]


def contains_a(item):
    return item["name"][0] == "a"


print(list(filter(contains_a, name_set)))

# zip
list_a = ["name", "hp", "class"]
list_b = ("Archer", 200, "Mage")

print(list(zip(list_a, list_b)))

# reduce
list_reduce = {1, 2, 3, 4, 5}


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, list_reduce, 0))
