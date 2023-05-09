n, m = map(int,input().split())
array = list(map(int, input().split()))

start= 0
end = max(array)
result = 0

#시작점과 끝점, 중간점 설정하여 잘라서 저장해보기
while(start<=end):
    total = 0 #자른것들 다 합한 값
    mid = (start+end)//2
    for x in array: #떡을 돌아가면서 자르면서보기
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1 #부족하니 end를 미드로 변경해 다시 
    else:
        result = mid #mid값 일단저장
        start = mid+1 #오른쪽 탐색 (최대한 적게가야하니까)

print(result)

