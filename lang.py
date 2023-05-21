class ProgrammingLanguage:

    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.poem = open("thepoem.txt", 'r').read()
    def call(self, text):
        print(text)
    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def dagger(self, a, b):
        return a * b
    def pival(self):
        from math import pi
        return pi
    def power(self, a ,b):
        return a ** b
    def slash(self, a, b):
        return a / b
    def remind(self, a, b):
        return a % b
    def sqrt(self, num):
        from math import sqrt
        n = sqrt(num)
        return n
    def hello(self, name):
        print(f"Hello {name} SIR.")
    def read(self, prompt):
        a = input(prompt)
        return a
    class check:
        def __init__(self, name, version):
            self.name = name
            self.version = version
        def type(self, variable, typ):
            if typ == 'str':
                if isinstance(variable,str):
                    return "yes"
                else:
                    return "Not a string"
            elif typ == 'int':
                if isinstance(variable, int):
                    return "yes"
                else:
                    return "Not an integer"
            elif typ == 'bool':
                if isinstance(variable, bool):
                    return "yes"
                else:
                    return "Not a boolean"
            elif typ == 'float':
                if isinstance(variable, float):
                    return "yes"
                else:
                    return "Not a string"
            else:
                return f"{typ} type not understood."
        def great(self, a, b):
            if a >= b:
                return "great or equalto"
            else:
                return False
        def less(self, a, b):
            if a <= b:
                return "less or equalto"
            else:
                return False
        def equal(self, a, b):
            if a == b:
                return "Equal"
            else:
                return False
        def notequal(self, a, b):
            if a != b:
                return "not equal"
            else:
                return False
        def inv(self, textin, var):
            return textin in var
        def indk(self, textin, var):
            return textin in var.keys()
        def indv(self, value, var):
            return value in var.values()
    

'''
py = ProgrammingLanguage("Python", "4.0")
check = py.check("Python", "4.0")

py.call(f"{py.name}-{py.version}")

name = py.read("Enter your name: \n>>>")
age = int(py.read("Enter your age: \n$$$"))
py.call(f"hello world {name} and you're {age} old.")

add = py.sum(12, 12)
sub = py.sub(100, 10)
mult = py.dagger(12, 12)
div = py.slash(12, 4)
pivalue = py.pival()
power = py.power(2, 4)
root = py.sqrt(81)
reminder = py.remind(12, 5)

py.hello(name)

lst = ["apple", "orange", "papaya", "litchi", "banana"]
dic = {"apple":12,"orange":10,"papaya":18}
tup = ("apple", "kiwi", "pomegranate")
qwerty = set(tup)
var = "Python is the best language"

py.call(add)
py.call(sub)
py.call(mult)
py.call(div)
py.call(power)
py.call(pivalue)
py.call(root)
py.call(reminder)

add = str(add)

py.call("Type checking\n")

py.call(check.type(name, 'int'))
py.call(check.type(add, 'str'))
py.call(check.type(sub, 'bool'))
py.call(check.type(pivalue, 'float'))
py.call(check.type(power, 'something'))
py.call(check.type(age, 'int'))

py.call("Operators\n")

py.call(check.equal(1, 1))
py.call(check.notequal(2, 0))
py.call(check.great(13, 12))
py.call(check.less(-1, 0))

py.call("Inside the variable or not\n")

py.call(check.inv('apple', lst))
py.call(check.inv('best', var))
py.call(check.inv('kiwi', tup))
py.call(check.indk('apple', dic))
py.call(check.indv(10, dic))
py.call(check.inv('something', qwerty))

py.call(py.poem)
'''
