
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
