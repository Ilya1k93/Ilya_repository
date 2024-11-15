n = int(input())
a = set()
output = []
for _ in range(n):
    m = list(map(int, input().split()))
    if m[0] == 1:
       a.add(m[1])
    elif m[0] == 2:
        if m[1] in a:
            output.append(1)
        else:
            output.append(0)
print(' '.join(map(str, output)))
