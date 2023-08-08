# 1. 기본 입력
# 2. 플로이드 워셜
# 3. 출력

#cost = 1 

# 1. 기본입력
INF = int(1e9)
n, m = map(int, input().split()) # 회사의개수 n, 경로의 개수 m
result = 0 # 결과적으로 소요값?
graph = [[INF]*(n+1) for _ in range(n+1)]

# 1-1. self by self reset to cost 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 1-2. graph info
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # a to b 's cost is c
    graph[b][a] = 1 # 서로에게 가는 비용이 1이라고 지정

x, k = map(int, input().split()) # 거쳐갈 x, 최종 k

# 2. 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        

# 3. 출력 ** 1-k + k-x  값을 지정 **

distance = graph[1][k]+ graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)