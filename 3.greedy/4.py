n, k = map(int, input().split())
result = 0

while True:
  #n이 k로 나누어 떨어지는 수 
  target = (n//k)*k #ex 27,4면 target = 6*4=24
  result += (n-target) #차이 3만큼 result값.
  n = target

  if n<k: #중간에 넣어준덴 이유가 있음
    break

  result +=1
  n //= k
#남은수 
result += (n-1)
print(result)