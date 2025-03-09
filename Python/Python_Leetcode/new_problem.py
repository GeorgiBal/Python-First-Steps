def reverseParentheses(s):
    stack = []
    for c in s:
        if c == ')':
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            for t in temp[::-1]:
                stack.append(t)
        else:
            stack.append(c)
    return "".join(stack)


print(reverseParentheses("(u(love)i)"))