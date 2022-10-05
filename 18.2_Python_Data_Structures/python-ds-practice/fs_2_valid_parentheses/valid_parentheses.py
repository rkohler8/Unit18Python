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
    tracker = 0
    for paren in parens:
        if paren == '(':
            tracker += 1
        elif paren == ')':
            tracker -= 1
        if tracker < 0:
            return False
    return tracker == 0

# DONE