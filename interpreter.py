from expressiongen import *
from tokenizer import *

inp = ""

while inp != "exit":
    inp = input("console:|>")
    if inp == "exit":
        break
    f = generateAtoms(inp)
    print(parseTree(expTree(infixToPostfix(tokenGenerator(f)))))
