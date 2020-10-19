from tokenobjects import *

def inorder(exp, s):
    if exp.type == "Variable":
        return exp.val
    else:
        s += inorder(exp.op1, "")
        s += exp.val
        s += inorder(exp.op2, "")
    return s

def genCode(parse):
    #print(parse.type, parse.val)
    if parse.type == "Variable" and parse.val == "0":
        #print("Hello?")
        return ""
    if parse.type == "Variable":
        return varCode(parse)
    elif parse.type == "FuncToken":
        return funCode(parse)
    elif parse.type == "BinOp":
        return opCode(parse)
    elif parse.type == "CallExp":
        return callCode(parse)
    elif parse.type == "IfToken":
        return ifCode(parse)

def ifCode(parse):
    s = 'if '
    s += "("
    s += inorder(parse.cond, "")
    s += ") {"
    for j in parse.exp:
        l = genCode(j)+";"
        # print(j, l)
        s += l
    s += "}"
    return s
    

def opCode(parse):
    return inorder(parse, "")

def varCode(parse):
    return inorder(parse.val,"")+";"

def funCode(parse):
    s = 'function '
    s += parse.name.val
    s += '('
    s += inorder(parse.arguments, "")
    s += ')'
    s += "{"
    #s += "\n"
    for j in parse.body:
        s += "\t"
        #print(s, j)
        s += genCode(j) + ";"
    s += "}"
    return s

def callCode(parse):
    s = parse.val
    s += "("
    #for i in parse.args:
    s += inorder(parse.args, "")
    s+= ")"

    return s

