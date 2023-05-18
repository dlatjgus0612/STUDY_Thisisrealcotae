n,x = map(int,input().split())
array = list(map(int, input().split()))

array.sort()
count = 0

#기본적인 선형탐색은 시간초과
# for i in array:
#     if i == x:
#         count += 1

#이진탐색으로 특정값의 마지막위치 - 첫번째 위치
from bisect import bisect_left, bisect_right
def count_by_range(array, left_value, right_value):
    return bisect_right(array, right_value)- bisect_left(array, left_value)

count = count_by_range(array, x, x) #둘다 x넣어주는게 포인트

if count == 0:
    print(-1)
else:
    print(count)