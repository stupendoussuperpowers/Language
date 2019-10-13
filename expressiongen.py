from tokenizer import *

def expTree(postfix):
    stack = []
    for i in postfix:
        if i.type == "Number":
            stack.append(i)
        else:
            i.subp = [None, None]
            i.subp[0] = stack.pop()
            i.subp[1] = stack.pop()
            stack.append(i)

    return stack.pop()

def traverseTree(root):
    if not root.subp:
        print(root)
    else:
        traverseTree(root.subp[0])
        print(root)
        traverseTree(root.subp[1])

def boolCheckfor(exp):
    return parseTree(exp).val

def parseTree(root):
    if root.type == "Number":
        return Token(type = "Number", val = root.val)
    else:
        if root.val == "?":
            if boolCheckfor(root.subp[1]):
                return parseTree(root.subp[0].subp[1])
            else:
                return parseTree(root.subp[0].subp[0])
        if root.val == "+":
            return Token(type = "Number", val = parseTree(root.subp[1]).val + parseTree(root.subp[0]).val)
        if root.val == "-":
            return Token(type = "Number", val = parseTree(root.subp[1]).val - parseTree(root.subp[0]).val)
        if root.val == "*":
            return Token(type = "Number", val = parseTree(root.subp[1]).val * parseTree(root.subp[0]).val)
        if root.val == "/":
            return Token(type = "Number", val = parseTree(root.subp[1]).val / parseTree(root.subp[0]).val)
        if root.val == ">":
            return Token(type = "Boolean", val = parseTree(root.subp[1]).val > parseTree(root.subp[0]).val)
        if root.val == "<":
            return Token(type = "Boolean", val = parseTree(root.subp[1]).val < parseTree(root.subp[0]).val)

def infixToPostfix(exp):
    post = []
    stack = []
    pred = {'+':1, '-':1, '*':2, '/':2, '(': -11, "?": -10, ">":-9, "<":-9, ":":-9}

    for i in exp:

        if i.type == "Number":
            post.append(i)

        elif i.val  == '(':
            stack.append(i)

        elif i.val == ')':
            while len(stack) > 0 and stack[-1].val != '(':
                post.append(stack.pop())
            stack.pop()

        else:
            while len(stack) > 0 and pred[i.val] < pred[stack[-1].val]:
                post.append(stack.pop())
            stack.append(i)

    while len(stack) > 0:
        post.append(stack.pop())

    return post


if __name__ == "__main__":
    f = tokenGenerator(generateAtoms("5 > 6 ? 7: 11"))
    g = infixToPostfix(f)
    #print(f.val)
    #print(f.subp[0].val)
