import re


def to_int(num):
    return eval(num) if is_num(num) else vars[num]


def is_num(num):
    return re.match('[-+]?[0-9.]+\\b', num)


def is_var(ss):
    return ss.isalpha()


def parse(str):
    str = str.replace('=', ' = ')
    str = str.replace('---', '-')
    str = str.replace('--', '+')
    str = re.sub('[+]+', '+', str)
    str = re.sub('[*/]{2,}', '##', str)
    for w in '+*/()=':
        str = str.replace(w, f' {w} ')
    str = re.sub('\\s+', ' ', str)
    return str.strip()


def isvalid(exp):
    parts = exp.split(' ')
    try:
        if parts.count('=') > 1:
            raise Exception('Invalid assignment')
        if re.match(".*[#*/]{2,}", exp):
            raise Exception('Invalid expression')
        if parts.count('(') != parts.count(')'):
            raise Exception('Invalid expression')
        return True
    except Exception as err:
        print(err)
        return False


def calc(exp):
    res = 0
    is_calc = False
    is_ass = False
    p = []  # stack
    for s in exp:
        if s in '+-*/=':
            is_calc = True
            is_ass = is_ass or s == '='
            op1 = p[-2]
            op2 = p[-1]
            if s == '=':
                assign(op1, op2)
            else:
                o1 = to_int(op1)
                o2 = to_int(op2)
                res = eval(str(o1) + s + str(o2))
            p.pop()
            p[-1] = str(res)
        else:
            p.append(s)
    if not is_calc:
        v = p[-1]
        if is_num(v):
            res = v
        elif v in vars:
            res = vars[v]
        else:
            print("Unknown variable")
            return
    if not is_ass:
        print(round(res))


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


def push_by_prior(w):
    # add an operation w to stack or postfix in accordance with prior
    if len(stack) > 0:
        st = stack[-1]
        while prior[w] <= prior[st]:
            st = stack.pop()
            postfix.append(st)
            if len(stack) == 0:
                break
            st = stack[-1]
        stack.append(w)
    else:
        stack.append(w)


def infix_to_postfix(exp):
    infix = exp.split(' ')
    postfix.clear()
    for w in infix:
        if w in '(=':
            stack.append(w)
        elif w == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix.append(stack.pop())
            if len(stack) > 0:
                stack.pop()
            else:
                postfix.append(w)
        elif w in '+-*/':
            push_by_prior(w)
        elif w != ' ':
            postfix.append(w)
    while len(stack) > 0:
        postfix.append(stack.pop())
    if '(' in postfix or ')' in postfix:
        postfix.clear()


vars = {}
stack = []
postfix = []
prior = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}

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
                infix_to_postfix(exp)
                calc(postfix)
print('Bye!')
