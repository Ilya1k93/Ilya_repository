n, m = map(int, input().split())
adj1 = [[0] * n for _ in range(n)]
adj2 = [[0] * n for _ in range(n)]

for _ in range(m):
    route = list(map(int, input().split()))
    k = route[0]
    stops = route[1:]
    for i in range(k - 1):
        u = stops[i] - 1
        v = stops[i + 1] - 1
        adj1[u][v] = 1
        adj1[v][u] = 1

    for i in range(k):
        for j in range(i + 1, k):
            u = stops[i] - 1
            v = stops[j] - 1
            adj2[u][v] = 1
            adj2[v][u] = 1

for row in adj1:
    print(' '.join(map(str, row)))
for row in adj2:
    print(' '.join(map(str, row)))
