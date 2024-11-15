n = int(input())
stack = []
output = []
for _ in range(n):
    m = input().strip().split()

    if len(m) == 2:
        _, x = m
        x = int(x)
        stack.append(x)
        output.append(stack[len(stack)-1])
    else:
        stack.pop()
        if len(stack) == 0:
            output.append(-1)
        else:
            output.append(stack[len(stack)-1])
print('\n'.join(map(str, output)))
