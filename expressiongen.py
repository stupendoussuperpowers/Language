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

def parseTree(root):
    if root.type == "Number":
        return root.val
    else:
        if root.val == "+":
            return parseTree(root.subp[0]) + parseTree(root.subp[1])
        if root.val == "-":
            return parseTree(root.subp[0]) - parseTree(root.subp[1])
        if root.val == "*":
            return parseTree(root.subp[0]) * parseTree(root.subp[1])
        if root.val == "/":
            return parseTree(root.subp[0]) / parseTree(root.subp[1])

def infixToPostfix(exp):
    post = []
    stack = []
    pred = {'+':1, '-':1, '*':2, '/':2, '(': 0}

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
    for i in infixToPostfix(tokenGenerator("5 + 9 * 7".split(" "))):
        print(i.val)
