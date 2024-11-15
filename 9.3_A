n = int(input())
d = {}
output = []
for _ in range(n):
    m = input().strip().split()
    
    if len(m) == 3:
        _, x, y = m
        x = int(x)
        y = int(y)
        d[x] = y
    elif len(m) == 2:
        _, x = m
        x = int(x)
        if x in d:
            output.append(d.get(x))
        else:
            output.append(-1)
        
print('\n'.join(map(str, output)))
