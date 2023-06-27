n = int(input()) 
array = list(map(int, input().split()))

dp = [1]*n #일단 하나씩은 다 갖고있으니까 

for i in range(n):
    dp[i]= d[i]+ d[i-1]
    dp[i]= d[i]+ max(d[i], d[i-1])
