def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []
    for paren in parens:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parentheses("()")) # True
print(valid_parentheses("()()")) # True
print(valid_parentheses("(()())")) # True
print(valid_parentheses(")()")) # False
print(valid_parentheses("())")) # False
print(valid_parentheses("((())")) # False
print(valid_parentheses(")()(")) # False
