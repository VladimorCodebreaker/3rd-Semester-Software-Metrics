import math


def load_exponent(first_arg, second_arg):
    if not (isinstance(first_arg, (int, float)) and isinstance(second_arg, (int, float))):
        raise TypeError(f"Result must be either [int] or [float]! {type(first_arg)} {type(second_arg)}")
    return math.ldexp(first_arg, second_arg)