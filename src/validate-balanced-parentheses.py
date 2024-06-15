# Time: O(n)
# Space: O(n)

class Solution:
    def isValid(self, s):
        openParens = ['(', '{' ,'[']
        closingParens = [ ')', '}', ']']

        stack = []

        for char in s:
            if char in openParens:
                stack.append(char)
            elif char in closingParens:
                if len(stack) <= 0:
                    return False
                if openParens.index(stack.pop()) != closingParens.index(char):
                    return False
        return len(stack) == 0
    

# Test
s = "()(){(())" # should return False
print(Solution().isValid(s))

s = "" # should return True
print(Solution().isValid(s))

s = "([{}])()" # should return True
print(Solution().isValid(s))
