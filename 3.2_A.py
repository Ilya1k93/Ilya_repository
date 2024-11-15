n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]

intervals.sort(key=lambda x: x[1])

count = 0
last_end = float('-inf')

for l, r in intervals:
      if l > last_end:
        count += 1
        last_end = r

print(count)
