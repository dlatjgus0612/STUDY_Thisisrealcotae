import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드개수, 간선개수 받기
n,m = map(int, input().split())
# start node
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n+1)]
# 방문 체크 리스트
visited = [False] *(n+1)
# reset by inf
distance = [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b노드 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 최단 거리 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0 # smallest index
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index #최단거리의 노드 번호를 반환
    

def dijkstra(start):
    # start node reset
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드 제외, 전체 n-1 개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 거 꺼내서 방문 처리.
        now = get_smallest_node()
        visited[now] = True
        # 현재 + 연결된 다른 노드
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드 거쳐서 다른 노드 가는게 더 짧으면
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력 
for i in range(1, n+1):
    # 도달 할 수 없는 경우 INF
    if distance[i] == INF:
        print("Infinity")
    # 도달할 수 있는 경우 출력
    else:
        print(distance[i])