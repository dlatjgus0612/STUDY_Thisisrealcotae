def dfs(graph, v, visited):
  #현재 노드 방문처리
  visited[v] = True
  print(v, end=' ')
  #현노드와 연결된 다른 노드 재귀적으로 방문하기
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited) #지금 i 방문처리 하고 돌리기 

graph = [
  [],
  [2,3,8], #1에 인접한 노드
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 
visited = [False]*9

dfs(graph, 1, visited)
