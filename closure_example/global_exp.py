# print(globals())

# globals()['x'] = 3

# # print(globals())


# def outer():
#     globals()['y'] = 'I am created from inside the outer func'
#     print(locals())
#     print(y)


# outer()

# print('y', 'I am available to to all scope of the program, because i am a global created from outer function')


# def second_outer():
#     global x
#     x = 34


# second_outer()

# print(x)


# def compose():
#     x = 12

#     def inner():
#         x += 1

#     inner()

# compose()


# def outer_data():
#     x = [1,2,3]

#     def modify_outer_data():
#         x.append(12)

#     modify_outer_data()

    # print(x)

# outer_data()


x = 12

def try_increase_x():
    global x
    x += 1

try_increase_x()
print(x)

def outer():
    x = 12 

    def inner():
        nonlocal x 
        x += 1
    
    inner()

    print(x)

outer()

