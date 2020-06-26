def BracketBalance(stringBrackets):
    """This function computes whether a string of brackets have equal number of open and closed brackets"""
    ##Check if all brackets come in pairs. If not, return False
    if "(" in stringBrackets:
        if stringBrackets.count("(") != stringBrackets.count(")"): return False##
    if "[" in stringBrackets:
        if stringBrackets.count("[") != stringBrackets.count("]"): return False
    if "{" in stringBrackets:
        if stringBrackets.count("{") != stringBrackets.count("}"): return False ##
   ##
    openBracs, closeBracs, stack = ["(","[","{"], [")","]","}"], [] ##
    for bracs in stringBrackets:
        if bracs in openBracs: stack.append(bracs) ##add opening brackets to stack
        else: ## else it's a close bracket so remove its corresponding open bracket
            if stack.pop() != openBracs[closeBracs.index(bracs)]:return False ##check if its the corresponding open bracket

    if len(stack)!=0: return False
    return True

print(BracketBalance("{{[}}]") )
