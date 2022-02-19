while True:
    cmd = input().strip()
    if cmd == '/exit':
        break
    if cmd:
        sum = 0
        numbs = map(int, cmd.split(' '))
        for num in numbs:
            sum += num
        print(sum)
print('Bye!')