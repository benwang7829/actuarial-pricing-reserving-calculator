def v(i, t):
    """
    Discount factor for t years at interest rate i
    """
    return 1 / (1 + i) ** t

