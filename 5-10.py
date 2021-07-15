print(">> n x m")
n, m = map(int, input().split())

# 0끼리 묶은 것들 카운팅
# 1. 특정 지점의 상하좌우 살피고 그 중 '0'이면서 아직 방문하지 않은 지점이 있다면 방문
# 2. 방문 지점에서 상하좌우 살피고 그 중 '0' 이면서 아직 방문하지 않은 지점이 있다면 방문.
# 1, 2.... 재귀적으로 수행

print(">> graph 정보")
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 범위를 벗어난 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문 처리

        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True

    return False  # 이미 방문한 노드면 false


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
