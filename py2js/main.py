from preparse import *
from parse import *
from codegen import *

testcodes = ['''
if a>b:
    c = a+b
    print("hello")
    if b<c:
        print("something")
    c = a-b
''',
'''
def helloworld(s):
    print(s)
'''
             ]

for s in testcodes:
    print(s)
    s = ''.join(i for i in handletabs(s))
    s = s.replace("\t","")
    # print(s)
    l = tokens(s)
    #print(l)
    q = parseExp(l)
    h = genCode(q)
    print(h)
