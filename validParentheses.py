# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Find the current opening bracket
# Search for the corresponding closing bracket
    # if wrong closing bracket, return false
    # if correct closing bracket, remove current opening & current closing

# if array is empty, return true

def isValid(s):
    dict = {"(": ")", "[": "]", "{": "}"}
    openingBrackets = []
    
    # Edge case for one character
    if len(s) == 1:
        return False

    # iterate through characters in the string
    for c in s:
        # if the character is an opening bracket
        if c == "(" or c == "[" or c == "{":
            openingBrackets.append(c)
        # if the character is a closing bracket
        else:
            if not openingBrackets:
                return False
            # check if matches current closing bracket
            if c != dict[openingBrackets[-1]]:
                return False
            else:
                openingBrackets.pop(-1)
    # if all brackets have been closed, return true
    return not openingBrackets

print(isValid('()'))