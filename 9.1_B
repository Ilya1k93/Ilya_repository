n, m = map(int, input().split())
room = [input() for _ in range(n)]
r, c = map(int, input().split())
q = int(input())
commands = input()

r -= 1
c -= 1

direction = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited_map = [[False] * m for _ in range(n)]
visited_map[r][c] = True

visited_positions = (r, c, None)
visited_count = 1

def position(head, row, col):
    return (row, col, head)

for cmd in commands:
    if cmd == 'L':
        direction = (direction - 1) % 4
    elif cmd == 'R':
        direction = (direction + 1) % 4
    elif cmd == 'M':
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == '.':
            r, c = nr, nc
            if not visited_map[r][c]:
                visited_map[r][c] = True
                visited_positions = position(visited_positions, r, c)
                visited_count += 1

print(visited_count)
