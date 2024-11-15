n = int(input())
m = list(map(int, input().split()))

def function(m):
    arg = m[0]
    j = 1
    for i in range(1,n):
        if m[i] <= arg:
            m[j], m[i] = m[i], m[j]
            j += 1
    m[0], m[j-1] = m[j-1], m[0]
function(m)
print(' '.join(map(str, m)))
