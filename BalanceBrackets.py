def BracketBalance(stringBrackets):
    """This function computes whether a string of brackets have equal number of open and closed brackets and if they're in the right order"""
    
    ###################
    if len(stringBrackets) == 1: return false ##if just one parantheses present in string
    
    stack = [] ##instantiate stack to hold parantheses
    
    for brac in stringBrackets:
        if (brac == '{' or brac == '[' or brac == '('):
            stack.append(brac) ##add every open parantheses in stack
            
        elif (c == '}' or c == ']' or c == ')'):
            if len(stack) == 0: return False ##return false because there is no corresponding open parantheses in stack
            
            else:
                ##check if each close parantheses has it's corresponding open parantheses in the right order. 
                ##else return false
                if (brac == ')' and  stack[-1]  == '('): stack.pop()
                    
                elif (brac == ']' and  stack[-1]  == '['): stack.pop()

                elif (brac == '}' and stack[-1]  == '{'): stack.pop()

                else: return false;

       return len(stack)==0; ##if stack is empty return True, else it's false because of unequal number of parantheses.



####Test
print(BracketBalance("{{[}}]") )
