n = int( input()) #가지고있는 부품개수 n
array = list(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))

# count = 0

# for i in range(n):
#     for j in range(m):
#         if arr2[j] ==arr1[i]:
#             count += 1

# if count != 0:
#     print('yes')
# else:
#     print('no')

#안된다... 왜지



#이진탐색 방법

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

array.sort()

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else: 
        print('no', end=' ')

#계수 정렬
#특정 수가 한번이라도 등장했는지를 검사하면됨 
#이빠이 큰 리스트 만들어놓고 인덱스별로 확인?
for i in x:
    if array[i]==1: #존재하는지
        print('yes', end=' ')
    else: 
        print('no',end=' ')

#집합 자료형
for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')
        