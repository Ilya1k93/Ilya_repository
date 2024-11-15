n = int(input())
stack = []
output = []
for _ in range(n):
    m = input().strip().split()

    if len(m) == 2:
        _, x = m
        x = int(x)
        stack.append(x)
        output.append(stack[0])
    else:
        stack.pop(0)
        if len(stack) == 0:
            output.append(-1)
        else:
            output.append(stack[0])
print('\n'.join(map(str, output)))
