"""
Python daily tips

I'll be explaining what list comprehension is, when you should use it and when you should not.

list comprehension is very power and makes writing for loops in a single line more pythonic.

So, when should I use list comprehension?

If you are working with a team, i will suggest using for loops because the team might contain 
developers with different programming backgorund like javascript, java, perl, c++, and using list comprehension 
can make things difficult for them to understand. 

When you're working on a personal project or in team of mid to seniors python developers, you can use list 
comprehension because they would all have had experience working with it. 

So, how can you write on?

Before i show you, i will create a list of items using for loops to fill the list and later use list comprehension 
to create the same list.  

"""

items = []

for i in range(10):
    items.append(i)

"""
In the above, we create empty variable list (variable assinged to a list) and loop over it using 
the range builtin function, the range will start from zero (0) to nine (9) and will be appending the 
number to the list in each iteration.
"""

# list comprehension
items2 = [i for i in range(10)]

"""
Writing same list using a single line of code. We create a variable called item2 and assigned it to a list, inside the
list, the first i, means the value that will be gotten from each iteration of the for loop and it will be separated 
with a comma automatically. The below show the build up for each iteration.

first loop. 
items2 = [0 for i in range(10)] 

In this case, i is 0. 

second iteration. 
items2 = [0, 1 for i in range(10)]

In this case, i is now 1 in the second iteration and will be automatically separated with comma from the value 
of the first iteration.

The above pattern will continue until the range gets to 9, at the end of the itration, 
the list will contain [0,1,2,3,4,5,6,7,8,9]

There are three template for creating a list comprehension 

1. x = [element for element in iterable]
2. x = [element for element in iterable if (condition)] // using if condition
3. x = [element (condition) for element in iterable] // using if / else condion
"""

# print(items)
# print(items2)


y_items = []
for i in range(10):
    if i % 2 == 0:
        y_items.append(i)

# print(y_items)

y_items2 = [i for i in range(10) if i % 2 == 0]
# print(y_items2)

z_items = []

for i in range(10):
    if i % 2 == 0:
        z_items.append(i)
    else:
        z_items.append(i/2)

print(z_items)

z_items2 = [i if i % 2 == 0 else i / 2 for i in range(10)]
print(z_items2)
