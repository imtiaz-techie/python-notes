def square(n):
    '''this is basically a docstring,not the comment! and it should be below on the function name(interview question)
    this program takes in a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

def square(n):
    print(n)
    '''this program takes in a number n,returns the square of n(this is not docstrings)''' #its not docstrings
    print(n**2)
square(5)
print(square.__doc__) #output is none