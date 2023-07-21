INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
# 2차원 리스트 (graph)표현. 무한으로 초기화

# self-self는 0으로 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선 정보 입력받아 값으로 초기화. 
for _ in range(m):
    # a에서 b가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] ==INF :
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()