from statementparse import *

f = open("pythontesting.py","r")
s = f.read()



def handletabs(s):

    s+="\n"
    s = s.replace(" "*4, "\t")
    s = s.split("\n")
    

    currenttabs = 0
    for ind, i in enumerate(s):
        if i != "":
            ttabs = 0
            for j in i:
                if j == "\t":
                    ttabs += 1
                else:
                    break
            if s[ind][-1] == ":" or s[ind] == "}":
                s[ind] = s[ind].replace(":", "")
            else:
                s[ind] += ";"
            if ttabs > currenttabs:
                s[ind] = "{" + s[ind].replace("\t", "")
            elif ttabs < currenttabs:
                s[ind] += "}"*(currenttabs-ttabs)

            currenttabs = ttabs
            print(currenttabs, i)
    return s

def tokens(string):
    i = 0
    buff = ""

    symbols = ['[','{',']','}','(',')','?',':',';']
    operators = ['+','-','*','/','.',',','=','>','<']
    
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

    print(atoms)

    tokenlist = []
    
    for i in atoms:
        if i in symbols:
            tokenlist.append(Token("Symbol", i))
        elif i in operators:
            tokenlist.append(BinOp(i))
        elif i == "if":
            tokenlist.append(IfToken("if"))
        elif i == "def":
            tokenlist.append(FuncToken())
        else:
            tokenlist.append(Token("Variable", i))

    
    return tokenlist


def parseIf(exp):
    i = 1
    cond = []

    while i < len(exp) and exp[i].val != "{":
        cond.append(exp[i])
        i+=1

    for _i in cond:
        print(_i)
    
    cond = parseExp(cond)
    print("here")
    body = []
    
    i+=1

    while i < len(exp) and exp[i].val != "}":
        body.append(exp[i])
        i+=1

    for _i in body:
        print(_i)
        
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
##        for i in cond:
##            print(i)
##        print("-"*80)
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

s = '''
if a>b:
    c = a+b
    print("hello")
    if b<c:
        print("something")
'''
s = ''.join(i for i in handletabs(s))
s = s.replace("\t","")
