def isValid(s):
    stack = []
    syb = ["[", "(", "{"]
    syb_cp = ["]", ")", "}"]
    if (len(s) % 2 != 0):
        return False
    for i in range(len(s)):
        if s[i] in syb:
            stack.append(s[i])
        else:
            if (not stack or syb_cp.index(s[i]) != syb.index(stack[-1])):
                return False
            stack.pop()
    return not stack


print(isValid("()[]{}"))
