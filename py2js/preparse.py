from tokenobjects import *

def handletabs(s):

    s+="\n0"
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
                s[ind] = "{"  + s[ind].replace("\t", "")
            elif ttabs < currenttabs:
                s[ind] += "}"*(currenttabs-ttabs)

            currenttabs = ttabs
            #print(currenttabs, i)
    #print(ttabs, currenttabs)
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

    #print(atoms)

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
