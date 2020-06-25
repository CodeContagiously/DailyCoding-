def BracketBalance(stringBrackets):
    """This function computes whether a string of brackets have equal number of open and closed brackets"""
    if "(" in stringBrackets:
        if stringBrackets.count("(") == stringBrackets.count(")"): pass ##if condition is met pass and proceed to other brackets
        else: return False
    if "[" in stringBrackets:
        if stringBrackets.count("[") == stringBrackets.count("]"): pass
        else: return False
    if "{" in stringBrackets:
        if stringBrackets.count("{") == stringBrackets.count("}"): return True ##on the last bracket return True if condition is met
        else: return False

"""Incomplete"""

print(BracketBalance("([)]") )
