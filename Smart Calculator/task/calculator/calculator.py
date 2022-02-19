while True:
    cmd = input().strip()
    if cmd == '/exit':
        break
    if cmd == '/help':
        print('The program calculates the sum of numbers')
    elif cmd:
        sum = 0
        numbs = map(int, cmd.split(' '))
        for num in numbs:
            sum += num
        print(sum)
print('Bye!')
