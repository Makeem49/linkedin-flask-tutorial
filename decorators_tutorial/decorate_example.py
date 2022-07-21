
def function_modyfier(condition):
    def decorated_func(original_func):
        def wrapper(*args):
            if condition == 'run':
                print('I can do additional stuff before calling the original function')
                value = original_func(*args)
                print(value)
                print('I can do additional stuff after calling the original function')
            else:
                return 'function cannot be run'
        return wrapper
    return decorated_func


@function_modyfier('run')
def original_func(x):
    return f'I will be invoked {x}'

print(original_func('now'))

# # super_charge_func = function_modyfier(original_func)
# # print(super_charge_func())

# def function_modyfier(func, argument):
#     def wrapper():
#         print('I can do additional stuff before calling the original function')
#         value = func(argument)
#         print(value)
#         print('I can do additional stuff after calling the original function')
#     return wrapper


# print(function_modyfier(original_func, 'now')())
   

