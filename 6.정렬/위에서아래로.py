n = int(input())
array = []
for i in range(n):  #enter로 값을 받고 싶으면 for 써야하더라
  array.append(input())
array = sorted(array, reverse=True)
for i in array:
  print(i, end=' ')
