#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
# in js the default value syntax is function(name: geeg, age: 8){ some value }
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
# /*args means you can pass in any argument
# /*args always has to be the last argument passed to a function
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# func1()
# Since there is no return value, it will print out 'I am a function' and then none, which
# is like undefined in JavaScript when there is no return value from a function
# print(func1())
# print(func1)
# func2(10, 20)
# print(func2(10, 20))
# print(cube(3))
# print(power(2))
# print(power(2, 3))
# print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4, 88))
