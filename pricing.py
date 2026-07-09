from mortality import qx, tpx
from interest import v

OMEGA = 150

def nex(age, t, i):
    """
    Pure endowment for t years at interest rate i on age 'age'
    """

    return v(i, t) * tpx(age, t)

def whole_life(age, i):
    """
    Whole life insurance at interest rate i on age 'age'
    """
    apv = 0
    for k in range(OMEGA - age):
        apv += v(i, k + 1) * tpx(age, k) * qx(age + k)

    return apv

def term_life(age, t, i):
    """
    Term life insurance for t years at interest rate i on age 'age'
    """
    apv = 0
    for k in range(t):
        apv += v(i, k + 1) * tpx(age, k) * qx(age + k)

    return apv

def endowment(age, t, i):
    """
    Endowment insurance for t years at interest rate i on age 'age'
    """

    return term_life(age, t, i) + nex(age, t, i)

def whole_life_annuity(age, i):
    """
    Whole life annuity at interest rate i on age 'age'
    """
    apv = 0
    for k in range(OMEGA - age):
        apv += v(i, k) * tpx(age, k)

    return apv

def temporary_life_annuity(age, t, i):
    """
    Temporary life annuity for t years at interest rate i on age 'age'
    """
    apv = 0
    for k in range(t):
        apv += v(i, k) * tpx(age, k)
    if t == 0:
        apv = 1

    return apv

def certain_and_life_annuity(age, t, i):
    """
    Certain-and-life annuity-due for t years certain.
    """
    certain_part = ((1 - v(i, t)) / i) * (1 + i)
    life_part = nex(age, t, i) * whole_life_annuity(age + t, i)

    return certain_part + life_part

