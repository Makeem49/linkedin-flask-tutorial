
from logging import raiseExceptions
from os import abort


num = 10
name = 'john'
# print(globals())

def outer(y):
    x = 3
    a = 10
    def inner(z):
        v = x * y * z
        return v
    return inner 


# print(outer.__code__.co_cellvars)
# print(outer.__code__.co_argcount)
# calculate_num = outer(5)
# print(calculate_num.__code__.co_freevars)
# print(calculate_num.__closure__[0].cell_contents)
# print(calculate_num.__closure__[1].cell_contents)


# print(calculate_num(2))

# def call_func(func):
#     count = 1

#     def count_func(num):
#         nonlocal count # this must be stated at the beginning of the inner function
#         if count < 4:
#             count += 1
#             return func(num)
#         else:
#             raise AttributeError('Function cannot be called more than four (3) times')
#     return count_func

# x = call_func(lambda num : num * 2)
# print(x(4))
# print(x(3))
# print(x(7))

def create_generator(array):
    count = 0 

    def custom_generator():
        nonlocal count 
        if count < len(array):
            value = array[count]
            count += 1
            return value 
        else:
            return f'{array[count - 1]} is the last number in the sequence'

    return custom_generator

gen = create_generator([1,2,3,4,5,6])

gen()
gen()
gen()
gen()
print(gen())
print(gen())
print(gen())
print(gen())


