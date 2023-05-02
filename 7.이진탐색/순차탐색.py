def sequential_search (n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
print ("생성할 원소 개수 입력, 찾을 문자열 입력")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("적은 원소 개수 만큼 문자열 입력. 구분은 공백하나")
array = input().split()

print(sequential_search(n, target, array))