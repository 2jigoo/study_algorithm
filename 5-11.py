from collections import deque

print(">> n x m")
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# N x M 크기의 직사각형 형태의 미로
# 괴물 있 0, 없 1
# (1, 1)에서 출발해서 (N, M)의 출구까지의 최단 경로의 칸 갯수 (시작 칸, 마지막 칸 포함)
# 칸의 개수가 필요하니까, 이동거리를 기록하면서 가야함.


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        # visited[]
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어남
            if nx < 0 or ny < 0 or nx >= n or ny >= m:

                continue

            # 벽
            if graph[nx][ny] == 0:
                continue

            # 아직 가보지 않은 길
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 최단 거리(현재까지 이동한 거리) 기록
                queue.append((nx, ny))

        return graph[n-1][m-1]

# (0, 0)에서 출발. 출구는 (n-1, m-1)에 있음
print(bfs(0, 0))