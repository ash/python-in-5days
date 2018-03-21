# Using an alternative testing framework, 'pytest'

import pytest

def fact(n):
    """This function does ..."""
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def test_fact_1():
    assert fact(1) == 1

def test_fact_2():
    assert fact(2) == 4

def test_fact_3():
    assert fact(5) == 120
