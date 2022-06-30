class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pointer = 0
        
        # odd number should be wrong
        if len(s) % 2 != 0:
            return False
        
        else:
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                    pointer = len(stack) - 1
                
                elif i == ')' and stack == []:
                    return False
                
                elif i == ']' and stack == []:
                    return False
                
                elif i == '}' and stack == []:
                    return False
                
                elif i == ')' and stack[pointer] != '(':
                    return False
                
                elif i == ']' and stack[pointer] != '[':
                    return False
                
                elif i == '}' and stack[pointer] != '{':
                    return False

                elif i == ')'  and stack[pointer] == '(':
                    stack.pop()
                    pointer = len(stack) - 1

                elif i == ']'  and stack[pointer] == '[':
                    stack.pop()
                    pointer = len(stack) - 1

                elif i == '}'  and stack[pointer] == '{':
                    stack.pop()
                    pointer = len(stack) -1
        
        if stack == []:
            return True
        
        else:
            return False
