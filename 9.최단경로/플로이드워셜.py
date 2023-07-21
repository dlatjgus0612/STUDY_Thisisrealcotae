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