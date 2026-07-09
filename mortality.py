import math

# Makeham parameters
A = 0.00022
B = 0.0000027
C = 1.124


def tpx(age, t):
    """
    Probability that a life aged 'age'
    survives t years.
    """
    exponent = (
        -A * t
        - (B * (C ** age) / math.log(C))
        * ((C ** t) - 1)
    )

    return math.exp(exponent)


def tqx(age, t):
    """
    Probability that a life aged 'age'
    dies within t years.
    """
    return 1 - tpx(age, t)


def px(age):
    """
    One-year survival probability.
    """
    return tpx(age, 1)


def qx(age):
    """
    One-year death probability.
    """
    return tqx(age, 1)