import re


def parse(str):
    str = str.replace('=', ' = ')
    str = str.replace('---', '-')
    str = str.replace('--', '+')
    str = re.sub('[+]+', '+', str)
    str = re.sub('\\s+', ' ', str)
    return str


def is_num(num):
    return re.match('[-+]?[0-9]+\\b', num)


def is_var(ss):
    return ss.isalpha()


def calc(exp):
    res = 0
    op = '+'
    for s in exp.split(' '):
        if s in '+-':
            op = s
        else:
            if is_var(s):
                s = str(vars[s])
            if op == '+':
                res += int(s)
            elif op == '-':
                res -= int(s)
            else:
                res = int(s)
    return res


def isvalid(exp):
    parts = exp.split(' ')
    i = 0
    is_ass = '=' in exp
    try:
        if parts.count('=') > 1:
            raise Exception('Invalid assignment')
        if len(parts) == 1 and not is_num(exp):
            if not is_var(exp):
                raise Exception('Invalid identifier')
            elif exp not in vars:
                raise Exception('Unknown variable')
        for p in parts:
            if is_ass and i % 2 == 0 and not is_var(p):
                if i == 0:
                    raise Exception('Invalid identifier')
                elif not is_num(p):
                    raise Exception('Invalid assignment')
            if i % 2 == 0 and not (is_var(p) or is_num(p)):
                raise Exception("Invalid expression")
            if i % 2 != 0 and not p in '+-=':
                raise Exception("Invalid expression")
            i += 1
        return True
    except Exception as err:
        print(err)
        return False


def assign(key, val):
    try:
        if not is_var(key):
            raise Exception("Invalid identifier")
        if not is_num(val) and not is_var(val):
            raise Exception("Invalid assignment")
        if not is_num(val) and val not in vars:
            raise Exception("Unknown variable")
        vars[key] = int(val) if is_num(val) else vars[val]
    except Exception as err:
        print(err)


vars = {}

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
                if '=' in exp:
                    e = exp.split(' ')
                    assign(e[0], e[2])
                else:
                    print(calc(exp))
print('Bye!')
