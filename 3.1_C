def function(n, k):
    n_m = n + k - 1
    n_f = n + k - 1
    n_k = n_f - k
    k_f = k
    for i in range(1, n_f):
        n_f = n_f * i
    if n_m == k:
        n_k = 1
    else:
        for j in range(1, n_k):
            n_k = n_k * j
    for g in range(1, k):
        k_f = k_f * g
    answer = n_f / (k_f * n_k)
    return answer

n, k = map(int, input().split())
print(int(function(n, k)))
