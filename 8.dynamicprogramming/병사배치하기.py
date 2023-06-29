n = int(input()) 
array = list(map(int, input().split()))
#뒤집어서 최장 증가 부분 수열 문제로 전환
array.reverse()

dp = [1]*n #일단 하나씩은 다 갖고있으니까 

#LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n- max(dp))