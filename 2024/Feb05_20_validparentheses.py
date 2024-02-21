"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

##########################
# First Solution Attempt #
##########################

"""
I started working on this one using a bunch of if statements and then realized that it was probably a stack
problem. 

Took me a few iterations because I missed the edge cases of "[" and "]"
"""
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([]{()})",
    "[",
    "]"
]

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for token in s:
            if token in "([{":
                stack.append(token)
            else:
                try:
                    opened = stack.pop()
                except IndexError:
                    return False

                if opened == "(" and token == ")":
                    pass
                elif opened == "[" and token == "]":
                    pass
                elif opened == "{" and token == "}":
                    pass
                else:
                    return False
                
        if len(stack) > 0:
            return False
        else:
            return True

solution = Solution()
for test_case in test_cases:
    print(solution.isValid(test_case))

"""
ACCEPTED
    Runtime
    41ms
    Beats 33.38% of users with Python3

    Memory
    16.62MB
    Beats 59.29% of users with Python3
"""

x = [[]]*3
for i, l in enumerate(x):
    l.append(i)

print(x)