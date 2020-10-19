
class Token(object):

    def __init__(self, ttype, val, subp = None):
        self.type = ttype
        self.val = val
        self.subp = subp

    def __str__(self):
        return "{Type: " + self.type + " Val:" +str(self.val)+"}"

class VarDecl(object):

    def __init__(self, val = None):
        self.type = "VarDecl"
        self.val = val

    def __str__(self):
        return "{"+"Type: {} Val: {}".format(self.type, self.val) + "}"

class LibExp(object):

    def __init__(self, val = None, sublib = None):
        self.type = "LibExp"
        self.val = val
        self.sublib = sublib

    def __str__(self):
        return "{"+"Type: {} Val: {} Sublib: {}".format(self.type, self.val, self.sublib) + "}"


class CallExp(object):

    def __init__(self, val = None, args = None):
        self.type = "CallExp"
        self.val = val
        self.args = args

    def __str__(self):
        return "{"+"Type: {} Val: {} Args: {}".format(self.type, self.val, self.args) + "}"
    
class BinOp(object):

    def __init__(self, val, op1 = None, op2 = None):
        self.type = "BinOp"
        self.val = val
        self.op1 = op1
        self.op2 = op2

    def __str__(self):
        return "{"+"Type: {} Val: {} Op1: {} Op2: {}".format(self.type, self.val, self.op1, self.op2)+"}"


class IfToken:
    def __init__(self, val, cond=None, exp=None, stelse=None):
        self.type = "IfToken"
        self.val = val
        self.cond = cond
        self.exp = exp
        self.stelse = stelse

    def __str__(self):
        return "{"+"Type:{} Val:{} Cond:{} Exp:{} Else:{}".format(self.type, self.val, self.cond, self.exp, self.stelse)+"}"

class FuncToken:

    def __init__(self, name = None, arguments = None , body = None):
        self.type = "FuncToken"
        self.name = name
        self.arguments = arguments
        self.body = body
        self.val = None

    def __str__(self):
        return "{"+"Type:{} Name: {} Arguments: {} Body: {}".format(self.type, self.name, self.arguments, self.body)+"}"

def tokens(string):
    i = 0
    buff = ""

    symbols = ['[','{',']','}','(',')','>','<','?',':',';']
    operators = ['+','-','*','/','.',',','=']
    
    atoms = []

    while i < len(string):
        if string[i] == " ":
            if buff != "":
                atoms.append(buff)
            buff = ""
        elif string[i] in symbols or string[i] in operators:
            atoms.append(buff)
            atoms.append(string[i])
            buff = ""
        else:
            buff += string[i]
        i+=1

    atoms.append(buff)

    for i in atoms:
        if i == "":
            atoms.remove(i)

    tokenlist = []
    
    for i in atoms:
        if i == "var":
            tokenlist.append(VarDecl())
        elif i in symbols:
            tokenlist.append(Token("Symbol", i))
        elif i in operators:
            tokenlist.append(BinOp(i))
        elif i == "if":
            tokenlist.append(IfToken("if"))
        elif i == "function":
            tokenlist.append(FuncToken())
        else:
            tokenlist.append(Token("Variable", i))

    
    return tokenlist

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

def parseVar(exp):
    if len(exp) > 3:
        return Token("Variable", parseExp(exp[1:]))
    else:
        return Token("Variable", exp[1])


def parseIf(exp):
    i = 1

    cond = []

    while i < len(exp) and exp[i].val != "(":
        i+=1

    i+=1

    while i < len(exp) and exp[i].val != ")":
        cond.append(exp[i])
        i+=1

    cond = parseExp(cond)

    body = []
    
    i+=2

    while i < len(exp) and exp[i].val != "}":
        body.append(exp[i])
        i+=1
    
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
        #if exp[i].type == "Variable":
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
    elif exp[0].type == "Variable" and (len(exp) > 1 and exp[1].type == "Symbol"):
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

h = parseExp(tokens("if ( 5>6) { 5+6-2; 78*9; }"))

def inorder(exp, s):
    if exp.type == "Variable":
        return exp.val
    else:
        s += inorder(exp.op1, "")
        s += exp.val
        s += inorder(exp.op2, "")
    return s

def genCode(parse):

    if parse.type == "Variable":
        return varCode(parse)
    elif parse.type == "FuncToken":
        return funCode(parse)
    elif parse.type == "BinOp":
        return opCode(parse)
    elif parse.type == "CallExp":
        return callCode(parse)
    

def opCode(parse):
    return inorder(parse, "")

def varCode(parse):
    return inorder(parse.val,"")

def funCode(parse):
    s = 'def '
    s += parse.name.val
    s += '('
    s += inorder(parse.arguments, "")
    s += ')'
    s += ":"
    s += "\n"
    for j in parse.body:
        s += "\t"
        s += genCode(j)

    return s

def callCode(parse):
    s = parse.val
    s += "("
    #for i in parse.args:
    s += inorder(parse.args, "")
    s+= ")"

    return s


data = ''
with open("inputtest.txt", "r") as f:
    data = f.read().replace("\n", "")
things = parseBody(tokens(data))
