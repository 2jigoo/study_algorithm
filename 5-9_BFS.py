from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 기록할 리스트
visited = [False] * 9

# 1번 노드부터 bfs 탐색
bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6

# 큐에 1 넣으면서 방문처리
# popleft() -> 1의 인접 노드인 2, 3, 4 큐에 넣으면서 방문 처리 [2, 3, 8]
# popleft() -> 2의 인접 노드 1, 7 중 미방문 노드 7 큐에 넣고 방문처리 [3, 8, 7]
# popleft() -> 3의 인접 노드 1, 4, 5 중 미방문 노드 4, 5 큐에 넣고 방문처리 [8, 7, 4, 5]
# popleft() -> 8의 인접 노드 2, 6, 8 중 미방문 노드 6 큐에 넣고 방문 처리 [7, 4, 5, 6]
# 모든 노드 방문 완료! 나머지 다 popleft()