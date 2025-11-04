def derive(coeff:int, exp:int)->str: 
    """Given two numbers, give the derivative
    """
    return f"{coeff * exp}x^{exp - 1}"