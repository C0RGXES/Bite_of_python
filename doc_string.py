def foo(x=1):
    """
    This is my function
    """
    return x + 1


# docstring return the comment at the begin of the function
print(foo(5).__doc__) # return the __doc__ string, because foo(5) is equal as 5, type int
print(foo.__doc__) # return the comment at the begin of the function foo()
