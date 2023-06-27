x = int(input())

# 26 25 5 1
# 26 13 12 6 2 1
# 26 13 12 4 2 1
#먼저 나눌수 있으면 나누는 게 좋고 아니면 빼고 들어가는게 좋은건 그리디
#이건 다를 수도 있음. 값이 적은것으로 update하는 것이 중요 

d = [0]*30001 #dptable초기화
#4가지 경우중 가장 적은 값을 골라서 거기에 1을 더해 넣는 (점화식)
#dynamic programmming - bottomup
for i in range(2, x+1): # 1은 이미 끝났다는 가정하에 2부터 시작 
    # 1을 빼는 경우
    d[i] = d[i-1]+1
    #2
    if i% 2 ==0 :
        d[i] = min(d[i],d[i//2]+1)
    #3
    if i% 3 ==0 :
        d[i] = min(d[i],d[i//3]+1)
    #5
    if i% 5 ==0 :
        d[i] = min(d[i],d[i//5]+1)

print(d[x])
