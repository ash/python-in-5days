# A module that has a function that we test with unittests and pytest

def fact(n):
    """This function does ..."""
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
