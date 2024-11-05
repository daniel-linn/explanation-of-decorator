# Prerequisites: Having a basic understanding of functions in python 

# How decorators works
# Decorators are like wrapping or packing a present, you wrap it with the first layer, then the second.
# Instead of wrapping paper, a decorator can add additional features to your original function, 
# without changing your code. It is very useful for functions need the same code added 
# to implement a certain design, like checking if user is logged in.

# How decorators are applied
# It's a bit tricky to understand how decorators are applied and executed. Code below shows how the actual 
# execution order of multiple decorators. As you can see, the applied order is from bottom to top,
# but the execution order is still from top to bottom.


# You can try it if you interested
'''
def a_new_decorator(f):
    def wrapTheFunction():  
        print('wrapping_1')
        f()
        print('wrapped_1')
        return f        
    return wrapTheFunction

def second_new_decorator(f):
    def wrapTheFunction():
        print('wrapping_2')
        f()
        print('wrapped_2')
        return f   
    return wrapTheFunction

# Executing section
print('processing')
@a_new_decorator
@second_new_decorator
def sim_func():
    print('function called')


sim_func()

# result:
# processing
# wrapping_1
# wrapping_2
# function called
# wrapped_2
# wrapped_1
'''

# Let's take another example

def new_decorator_v2(f):
    print('wrapping_1')
    return f

def second_new_decorator_v2(f):
    print('wrapping_2')
    return f

def decorated_func():
    print('function called')

decorated_func = new_decorator_v2(second_new_decorator_v2(decorated_func))
decorated_func()

# This line new_decorator_v2(second_new_decorator_v2(decorated_func)) equals:
# @new_decorator_v2
# @second_new_decorator_v2
# def decorated_func():
#     print('function called')
#
# decorated_func()
#
# As you see, python dose read the code from top to bottom
# 
# the result is:
# wrapping_2
# wrapping_1
# function called
# 
# For beginner-friendly and easy-to-understand explanations, the term 'call' is replaced with 'execute'
#
# What's happening here, and why does the order seem reversed from the expected execution order?
# The secret is the () symbol, （）is part of the function call syntax
# You may be familiar with this concept: Everything in Python is Object, even functions.
# So function can be object, just like any other variable, 
# you can also make a variable to a function object, as we have done above
# Only when you use (), the code in function will be actual called, in other words, executed
#
# Now take a look at the line of how we turn decorated_func into a decorated function(or, make it into a new function object)
# What dose new_decorator_v2(...) mean? It means we're executing the function with the parameter inside ()
# Then, what's in the ()? as you can see, it's second_new_decorator_v2(...)
# Here's where something interesting happens, even though second_new_decorator is a parameter of new_decorator_v2
# But since we use () for second_new_decorator, it means the second_new_decorater will also been executed
# And since it located inside (), that means it will be executed first before the code inside the new_decorator_v2,
# since python need to know what is the parameter in the (), then it can bring it to the code inside the function(that is, new_decorator_v2)
#
# Now we know that second_new_decorator_v2 will execute first due to (), but executes with what?
# the second_new_decorator_v2 takes a parameter 'decorated_func', it's a function, but this time, we don't use (),
# meaning the function won't execute, instead, it acts as a parameter of second_new_decorator_v2
#
# Now things are more clearer: second_new_decorator_v2 executes first, prints something, 
# and returns the function 'decorated_func' to new_decorator_v2. 
# Then new_decorator_v2 takes decorated_func as a parameter, executes, print something, 
# and returns the decorated_func
# Finally, since we use decorated_func(), the function executes after all of this, 
# or we could say, it's decorated
