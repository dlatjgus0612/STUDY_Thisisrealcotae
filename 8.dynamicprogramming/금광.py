# test case
for tc in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))

    # dptable reset
    dp = []

    # 금광정보가 한줄로 들어가기에 
    #열만큼 slicing 하여 넣어주는 작업 
    index = 0 
    for i in range(n):
        dp.append(array[index:index+m]) 
        index += m 

    #dynamic programming
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우 
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0 
    for i in range(n): #가장 오른쪽 열에서 가장 큰것을 출력하도록
        result = max(result, dp[i][m-1])
    print (result)
