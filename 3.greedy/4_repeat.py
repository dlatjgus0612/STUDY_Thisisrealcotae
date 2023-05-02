n, k = map(int, input().split())
result = 0

#되는 것에 적용 시켜야하므로 while 문 사용
# while True: #if 25, 5면
#   if (n%k != 0): #나머지가 있으면
#     target = int(n-1)
#     count += 1
#     break
#   else:
#     target = int(n)
#     count += (target/k)
#     break

# print(count)

while True:
  #n이 k로 나눠떨어지는 수
  target = (n // k) * k
  # 나누어 떨어지는 값중 최댓값으로 잡기
  # ex) 25, 5면 5*5 / 27, 4면 6*4
  result += (n - target)
  # ex) 0 / 3  -- 1을 빼줘야하는 값을 추가
  n = target  # ex) 25 / 27

  if n < k:  # 더이상 나눌수가 없어지면
    break

  result += 1
  n //= k
  # 몫 ex) 5 / 6 ==> 그리고 다시 올라가 반복?

result += (n - 1)
print(result)

#target에 대한 나머지 -->result
#target --> n  넣고 나누다가 안나눠질때 남은 값을 result 에 마지막에 더해주는 게 포인트
