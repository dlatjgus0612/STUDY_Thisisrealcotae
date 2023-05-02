n, m = map(int, input().split())
result = 0
for i in range(n):
  #열 X 행 으로 리스트로 받아서 총 data, min 중에서 max를 찾는 것 
  data = list(map(int, input().split()))
  minval = min(data)
  result = max(result, minval)

print(result)