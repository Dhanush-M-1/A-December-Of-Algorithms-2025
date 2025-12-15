from collections import deque

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))


islands = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            islands += 1

print(islands)
