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
