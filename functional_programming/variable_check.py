"""
Small integer caching , Variable identity and variable value 

OMG, why x is y evaluate to False and z is a  evaluate to True for the below code

x = 300
y = 300

z = 5 
a = 5

Well that' what I am going to explain in this post. 

Variable identity and variable value.

Creating a variable is as easy as assigning the right handside to the left handside. Is as simple as that.
"""

x = 5 # this is a variable 
y = 'Hello world'
items = [1,2,4,'hello world']
"""
For every variable created in python, it will create a location in memory where the value associated to the variable 
is stored. To be able to check that location in memory we call the id built-in function of the 
variable name, and that will return the variable identity. The return from the id may differ when running similar 
code. 
"""

print(id(x))  # / 9789088 is the variable identity 
print(id(y))  # / 140230757977136 is the variable identity 
print(id(items)) # / 140230758900224 is the variable identity 

"""
Those value return from the id built-in function are the variable identity for that particular variable. 
When you called the variable itself, the value return is the variable value. 

"""
print(x) # 5 is the variable value 
print(y) # "hello wworld"  is the variable value. 

"""

Guess the outcome of the code below without running the code. 

y = 300
x = 300

print(y is x ) 

"""
print(y is x )

"""
If you get the above snippet of code right good job, if not, this post is specifically for you. 

The reason why the above fail is that, in python, small integer value between [-5] to [256] will be cached. That is,
if you assign 1 to a variable called x, and later you assigned 1 to a variable called y, both of the variable is
reference the same value (in this case 1) in memory. Thus, both will have same variable identity. 
"""

x = 1
y = 1
print(x is y) # will be  True because both are pointing to same object in memory. 

a = -5 
b = - 5 
print(a is b ) # will be  True because both are pointing to same object in memory. 

c = 256
d = 256
print(c is d )  # will be  True because both are pointing to same object in memory. 

"""
But when u assigned anything less than -5 and anything greater than 256 will on two separate line, they will have 
different identity value, thus will result to false when using is operator to check them. 
"""

q = 303 
r = 303 
print(id(q)) 
print(id(r))
print(q is r)  # different variable identity thus return false

"""
One more gotcha. 

first, second = 302, 302

using the is operator will result to True because they both defined on the same line, so python will cache them 
to use a single memory location thus will result to having same memory identity. As soon as they are declared on a separate line, they will have different 
variable identiy. 
"""
first, second = 302, 302

print(id(first))
print(id(second))