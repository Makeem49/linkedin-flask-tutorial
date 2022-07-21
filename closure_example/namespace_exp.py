x  = 5
print(globals())

def outer():
    x = 20
    y = 30
    print(f'x inside outer is {x}')
    print(f'{locals()} inside outer')

    def inner():
        x = 40
        z = 12
        print(y)
        print(f'x inside inner is {x}')
        print(f'{locals()} inside inner') 

    inner()

outer()