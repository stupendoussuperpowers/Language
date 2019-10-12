from tokenizer import *

def expTree(postfix):
    stack = []
    for i in postfix:
        if i.type == "Number":
            stack.append(i)
        else:
            i.op2 = stack.pop()
            i.op1 = stack.pop()
            stack.append(i)

    return stack.pop()

def traverseTree(root):
    if not root.op1:
        print(root)
    else:
        traverseTree(root.op1)
        print(root)
        traverseTree(root.op2)

def parseTree(root):
    if root.type == "Number":
        return root.val
    else:
        if root.val == "+":
            return parseTree(root.op1) + parseTree(root.op2)
        if root.val == "-":
            return parseTree(root.op1) - parseTree(root.op2)
        if root.val == "*":
            return parseTree(root.op1) * parseTree(root.op2)
        if root.val == "/":
            return parseTree(root.op1) / parseTree(root.op2)

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
