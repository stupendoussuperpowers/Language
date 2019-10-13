from pprint import pprint

class Token:

    def __init__(self, type, val, subp = None):
        self.type = type
        self.val = val
        self.subp = subp

    def __str__(self):
        return "Name : " + self.type + " Val:" +str(self.val)

def generateAtoms(string):
    buff = ""
    out = []
    operators = ["+", "-", "/", "*", "(", ")", "<", ">","{","}", "?", ":"]

    for i in string:
        if i == " ":
            if buff != "" : out.append(buff)
            buff = ""
        elif i in operators:
            if buff != "" : out.append(buff)
            out.append(i)
            buff = ""
        else:
            buff += i

    out.append(buff)
    return out

def tokenGenerator(atoms):

    tokenlistfinal = []
    for i in atoms:

        if i.isdigit():
            tokenlistfinal.append(Token(type = "Number", val = int(i)))
        elif i == "?":
            tokenlistfinal.append(Token(type = "If", val = "?"))
        elif i == ":":
            tokenlistfinal.append(Token(type = "If", val = ":"))
        elif i == "{" or i == "}" or i == "(" or i == ")":
            tokenlistfinal.append(Token(type = "Bracket", val = i))
        elif i in ["*", "+","-","*", "/", "<", ">"]:
            tokenlistfinal.append(Token(type = "BinaryOp", val = i))

    return tokenlistfinal


if __name__ == "__main__":
    print("Nah Bruv")
    print(generateAtoms("5* 9 +    8"))
