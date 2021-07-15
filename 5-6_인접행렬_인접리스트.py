## 인접 행렬

INF = 99999999999 # 무한의 비용 선언

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)


## 인접 리스트

graph = [[] for _ in range(3)]

# (노드 번호, 거리)

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)