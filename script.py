"""Implementation of the LDEXP Function - SW Metrics Exam - Part 2"""
import math


def load_exponent(first_arg, second_arg):
    """Returns x * (2**i). This is the inverse of the function frexp()."""
    if not (isinstance(first_arg, (int, float)) and isinstance(second_arg, (int, float))):
        raise TypeError(f"Result must be either int or float! {type(first_arg)} {type(second_arg)}")
    if (isinstance(first_arg, bool) or isinstance(second_arg, bool)):
        raise TypeError(f"Arguments cannot be of type 'bool' ! {type(first_arg)} {type(second_arg)}")
    return math.ldexp(first_arg, second_arg)
