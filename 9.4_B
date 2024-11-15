n = int(input())
a = list(map(int, input().split()))

stack = []
left = [-1] * n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    else:
        left[i] = -1
    stack.append(i)

result = [i - left[i] - 1 for i in range(n)]
print(' '.join(map(str, result)))
