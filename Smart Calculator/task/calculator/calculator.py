import re


def parse(str):
    str = str.replace('---', '-')
    str = str.replace('--', '+')
    str = re.sub('[+]+', '+', str)
    str = re.sub('\\s+', ' ', str)
    return str


def isdig(num):
    if num[0] in '+-':
        return num[1:].isdigit()
    else:
        return num.isdigit()


def calc(exp):
    res = 0
    op = '+'
    for s in exp.split(' '):
        if isdig(s):
            if op == '+':
                res += int(s)
            elif op == '-':
                res -= int(s)
            else:
                res = int(s)
        else:
            op = s
    return res


def isvalid(exp):
    parts = exp.split(' ')
    i = 0
    for p in parts:
        if i % 2 == 0 and not isdig(p):
            return False
        if i % 2 != 0 and not p in '+-':
            return False
        i += 1
    return True


while True:
    cmd = input().strip()
    if cmd == '/exit':
        break
    if cmd == '/help':
        print('The program calculates the sum of numbers')
    elif cmd:
        if cmd[0] == '/':
            print("Unknown command")
        else:
            exp = parse(cmd)
            if isvalid(exp):
                print(calc(exp))
            else:
                print("Invalid expression")
print('Bye!')
