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
            else:  #checking if first bracket is closing i.e. (')', ']', '}') then it will return False
                return False

        if len(stack) == 0:
            return True
  

                    
                    


        