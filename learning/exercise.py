# class SuperList(list):
#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])

# lambda expressions
'''
lamda is an anonymous function that on ly runs once
# '''
# list_a = {5, 4, 3}

# print(list(map(lambda item: item**2, list_a)))

# list_b = [(0, 2), (4, 3), (9, 9), (10, -1)]

# list_b.sort(key=lambda item: item[1])
# print(list_b)

# list comprehension
# list_c = [num for num in range(0, 100)]
# list_d = [num**2 for num in range(0, 100)]

# list_only_even = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(list_only_even)

# dictionary comprehension
# simple_dict = {
#     "attack": 2,
#     "base_mp": 4
# }

# my_dict = {key: value**2 for key, value in simple_dict.items()}
# print(my_dict)

# decorator

from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1}ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000):
        i*5


long_time()
