import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #infinite. 무한
#노드개수, 간선개수, 시작노드번호 
n, m = map(int, input().split())
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n+1)]
# 최단, 거리 테이블 무제한으로 초기화
distance = [INF] *(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c 라는 의미
    graph[a].append((b,c))


# 기존에 현재를 확인하여 짧은 것을 선택하는 함수가 삭제.
# 힙을 이용하여 간편하게 
def dijkstra(start):
    q = []
    # 시작노드 최단경로 0 으로 설정하여 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q) #b, c, a
        # 이미 처리 된적 있으면 무시
        if distance[now] < dist:
            continue
        # 현재와 연결된 인접 노드 확인 
        for i in graph[now]: #인접 노드들 모드 확인 
            cost = dist + i[1] #dist(현재 확인하고있는 거리 ) + i[1] (거리값)
            # 갱신했는데 짧으면
            if cost < distance[i[0]]: #현재보다
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        # 도달할 수 있는 경우 거리 출력
        print(distance[i])