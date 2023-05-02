n, k = map(int, input().split())  #n (배열 원소 개수) , k (바꿔치기 가능 횟수)
a = list(map(int, input().split()))  #배열 A
b = list(map(int, input().split()))  #배열 B

a.sort()  #오름으로 정렬
b.sort(reverse=True)  #기본 내림차순 정렬

result = 0  #총합

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]

print(sum(a))
