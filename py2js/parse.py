from tokenobjects import *

def postfix(exp):
    post = []
    stack = []
    pred = {'.':-2,',':-1,'=':0,'+':1, '-':1, '*':2, '/':2, '(': -11, "?": -10, ">":-9, "<":-9, ":":-9}

    for i in exp:

        if i.type == "Variable":
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


def parseIf(exp):
    i = 1
    cond = []

    while i < len(exp) and exp[i].val != "{":
        cond.append(exp[i])
        i+=1

    #for _i in cond:
     #   print(_i)
    
    cond = parseExp(cond)
    #print("here")
    body = []
    
    i+=1

    while i < len(exp) and exp[i].val != "}":
        body.append(exp[i])
        i+=1

    #for _i in body:
        #print(_i)
        
    body = parseBody(body)

    return IfToken(exp[0].val, cond, body)

def parseFunc(exp):
    name = exp[1]

    j = 3
    arguments = []
    while j <len(exp) and exp[j].val != ")":
        arguments.append(exp[j])
        j+=1
    arguments = parseExp(arguments)
    j+=2

    body = []
    
    while j < len(exp) and exp[j].val != "}":
        body.append(exp[j])
        j+=1

    body = parseBody(body)

    return FuncToken(name, arguments, body)

def parseBody(exp):
    body = []
    i = 0
    j = 0
    while i < len(exp):
        cond = []
        while j < len(exp) and exp[j].val != ";":
            cond.append(exp[j])
            j+=1

        cond = parseExp(cond)
        
        body.append(cond)
        j+=1
        i = j

    return body
    

def parseCall(exp):
    name = exp[0].val
    i = 2

    arguments = []
    while i < len(exp) and exp[i].val != ")":

        arguments.append(exp[i])
        i+=1

    arguments = parseExp(arguments)
    
    return CallExp(name, arguments)
    

def parseExp(exp):
    tree = []
    if exp[0].type == "Symbol":
        tree.append(parseExp(exp[1:]))
    elif exp[0].type == "IfToken":
        tree.append(parseIf(exp))
    elif exp[0].type == "FuncToken":
        tree.append(parseFunc(exp))
    elif exp[0].type == "VarDecl":
        tree.append(parseVar(exp))
    elif exp[0].type == "Variable" and (len(exp) > 1 and exp[1].val == "("):
        tree.append(parseCall(exp))
    else:
        for i in exp:
            f = postfix(exp)
            for i in f:
                if i.type == "BinOp":
                    o2 = tree.pop()
                    o1 = tree.pop()
                    new = BinOp(i.val, o1, o2)
                    
                    tree.append(new)
                elif i.type == "Variable":
                    tree.append(i)
    return tree[0]
