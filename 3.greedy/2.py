#큰 수의 법칙
#n개의 배열 숫자를 받고, m개 숫자를 받아 큰 수 만들기, 반복 가능 횟수는 k. index만 다르면 같은숫자도 가능
n, m, k = map(int, input().split())  #공백 구분하여 정수 형 숫자 받기
data = list(map(int, input().split()))  #데이터 리스트 받기

data.sort()  #기본은 오름차순 정리
first = data[n - 1]
second = data[n - 2]

result = 0  #결과값 초기화 해두기

# solution 1 : k만큼 큰 거 더하고 그 다음 작은거 더해주기
while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1  #결과 구할때마다 1씩 빼기
  if m == 0:
    break
  result += second
  m -= 1

# solution 2 : [ 큰거*k + 작은거 ] 순열 찾아 곱하기
count = int(m / (k + 1)) * k
count += m % (k + 1)  #딱 나누어 떨어지지 않을 때의 나머지도 구해둔다

result += count * first
result += (m - count) * second

print(result)

#-----------------------------------------
n, m, k = map(int, input().split())  #변수 (받을배열 수, m번 더하기, k번 초과불가 )
data = list(map(int, input().split()))  #list 받기
data.sort()  #오름차순 정렬
first = data[n - 1]
second = data[n - 2]
# for _ in range (m//k):
#   result += first*(k-1)
# for _ in range (m%k):
#   result += second
#함수를 안써도 된다는 것...

#가장 큰수가 더해지는 횟수 계산 (m이 8, k가 3이면) 2 2 3 2 2 3 2 2
count = int(m / (k + 1)) * k  # 8/4=2 * 3 ==> 6
count += m % (k + 1)  #나머지 0  @@

result = 0
result += count * first
result += (m - count) * second  # @@

print(result)
