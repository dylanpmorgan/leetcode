import unittest
from copy import copy

"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

Example 2:
    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

Example 3:
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
"""

example_inputs = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ["3","11","5","+","-"]
]
example_outputs = [
    9, 6, 22, -13
]


##########################
# First Solution Attempt #
##########################
"""
Right off the rip, no idea how to start this one -- confused by the premise of the question and 
reverse polish notation.

I think...I'll start by trying to iterate through the list until I hit an operator and then move backwards to 
find digits to operate against
"""
# Operators we'll run into
operators = ["+", "-", "*", "/"]

# Helper function to make sure that the token is an integer. Probably not necessary but just in case
def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True


# Helper funtion to recursively iterate through the token list until an integer non-used token is found
def find_next_digit(tokens, index=0, used_loc=None):
    if index < 0:
        return (None, None)
    # print(f"looking for next digit: {index, tokens[index]}")
    if represents_int(tokens[index]) and index not in used_loc:
        return (index, tokens[index])
    else:
        index -= 1
        return find_next_digit(tokens, index=index, used_loc=used_loc)
    

def evalRPN_v1(tokens):
    # Catch edge case where there are no operators
    if len(tokens) == 1:
        return int(tokens[0])

    # Keep track of which tokens are used
    used_locs = set()
    # Define empty variables
    result = None
    first_operand_loc = None

    # Iterate through token list until all tokens are used
    while len(used_locs) < len(tokens):
        # List to hold the operations
        operation = list()
        # Iterate over token list and use enumerate for index
        for i, token in enumerate(tokens):
            # Check if the token is in the operator list
            if token in operators:
                # If so, track the operator
                operator_i = (i, token)
                # print(f"operator found: {operator_i}")
                
                # I want to store the result as we more operations continue but the first time it will be null
                if result is None:
                    first_operand_i = (i-2, tokens[i-2])
                    # this will help me know which order to do the operations in
                    first_operand_loc = i-2
                    # add this to the used locations so we can skip it
                    used_locs.add(first_operand_i[0])
                else:
                    # Keep track of the result and where it was first located
                    first_operand_i = (first_operand_loc, str(result))

                # print(f"first operand found: {first_operand_i}")
                # Recursively find the next unused digit
                second_operand_i = find_next_digit(tokens, index=operator_i[0]-1, used_loc=used_locs)
                # Just in case the recursive find_next_digit goes to the start of the list without finding a digit
                if second_operand_i[0] == None:
                    # print(f"Second operator is None: {second_operand_i}")
                    continue
                # print(f"second_operand found: {second_operand_i}")
                # Check the operand locations to know which order to do the operation
                if first_operand_loc < second_operand_i[0]:
                    result = eval(
                        "".join([first_operand_i[1], operator_i[1], second_operand_i[1]])
                    )
                    result = int(result)
                else:
                    result = eval(
                        "".join([second_operand_i[1], operator_i[1], first_operand_i[1]])
                    )
                    result = int(result)
                # Keep track of used tokens
                used_locs.add(operator_i[0])
                used_locs.add(second_operand_i[0])
            # print(result, used_locs)
    return result

for tokens, expected in zip(example_inputs, example_outputs):
    result = evalRPN_v1(tokens)
    print(f"Result: {result}\nExpected: {expected}")
    assert result == expected

"""
Failed multiple test cases and I kept trying to add fixes until it's clear this approach will not work.

I knew from the start that this solution would be horribly inefficient but I was already committed and needed to keep
trying so I could get a working solution in the 30 minute timelimit.

I went a little over the timelimit at 45 minutes.
"""


###########################
# Second Solution Attempt #
###########################
"""
My first solution attempt failed a few of the test cases before I threw in the tail and asked ChatGPT for a hint.

Turns out I was way off on my first attempt (chatgpt described it as "interesting and overlycomplex") -- this problem
can be easily solved using stack.

My second solution attempt will try to use a stack
"""
def evalRPN_v2(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            first = stack.pop()
            second = stack.pop()
            if token in "+":
                stack.append(first+second)
            elif token in "-":
                stack.append(second-first)
            elif token in "*":
                stack.append(first*second)
            else:
                # For division we want to make sure the result is truncated to zero -- which int() does
                stack.append(int(second/first))
        else:
            stack.append(int(token))

    return int(stack.pop())

for tokens, expected in zip(example_inputs, example_outputs):
    result = evalRPN_v2(tokens)
    print(f"Result: {result}\nExpected: {expected}")
    assert result == expected

"""
ACCEPTED
    Runtime
    61ms
    Beats 85.54% of users with Python3

    Memory
    17.09MB
    Beats77.53%of users with Python3

Pretty happy with those results! Too bad I couldn't think of that approach on my own...
"""