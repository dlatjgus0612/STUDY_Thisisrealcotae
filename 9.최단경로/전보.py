# 1. 정의 파트
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 2. function 파트 
    # dijkstra with heap
def dijkstra(start):
    q = [] 
    heapq.heappush(q, (0,start)) # 시작노드 0으로 시작, 큐 삽입
    d[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q) #b, c, a
        # 이미 처리 된적 있으면 무시
        if d[now] < dist:
            continue
        # 현재와 연결된 인접 노드 확인 
        for i in graph[now]: #인접 노드들 확인 
            cost = dist + i[1] #dist(현재 확인하고있는 거리 ) + i[1] (거리값 a(c))
            # 갱신했는데 짧으면
            if cost < d[i[0]]: #현재보다
                d[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))   

# 3. 입력 받기 
    # 도시개수, 통로개수, start
n, m, start = map(int, input().split())
    # 노드간 정보담는 list
graph = [[] for i in range(n+1)]
    # reset by INF
d = [INF] * (n+1)

    # xyz 입력 받기 (모든 간선 정보 입력받기)
    # xyz = [[map(int, input().split())] for _ in range(m)]
for _ in range(m): # x-> y 비용이 z라는 의미 
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) 

# 4. 실행과 출력 **
    # print (거리가 INF가 아닌것의 개수, max(z))
dijkstra(start)

    # 도달할 수 있는 노드의 개수, 그 중 멀리 있는 노드와의 (최단)거리 
count = 0
max_d = 0
for j in d: # 아싸리 거리중에서만 본다
    if j != INF:
        count += 1
        max_d = max(max_d, j)

print (count -1, max_d) 

