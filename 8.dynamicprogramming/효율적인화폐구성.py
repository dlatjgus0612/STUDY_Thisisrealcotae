n,m = map(int, input().split())
#array = [input().split() for _ in range(n)] 왜 안되지?
array = []
for i in range(n): 
    array.append(int(input()))

#dp table 초기화
d = [10001]*(m+1)
#dynamic programminng - bottomup
d[0]=0
for i in range(n): #i - 단위별로 돌면서
    for j in range(array[i], m+1): # j - 각각의 금
        if d[j-array[i]] != 10001: #(i-k)원을 만드는 방법이 존재
            d[j]= min(d[j], d[j-array[i]]+1) #지금 j의 값을 jvs 다른 어레이와 한것 -1 비교하여 업데이트?

if d[m] ==10001: #최종적으로 m원 만드는 방법이 없는 경우 
    print(-1)
else: print(d[m])