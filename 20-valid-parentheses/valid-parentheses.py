class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
  
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            elif i in [')', ']', '}']:
                return False


        if len(stack) > 0:
            return False
        else:
            return True
  

                    
                    


        