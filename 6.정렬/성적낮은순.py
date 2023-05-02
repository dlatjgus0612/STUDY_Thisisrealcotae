# N 입력 받기
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])  #람다로 새로 변수 지정해줘야 인식함

# 정렬이 수행된 결과를 출력
for student in array:
  print(student[0], end=' ')

#최적
# N 입력 받기
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = [input().split() for _ in range(n)]

# 점수를 기준으로 정렬
array.sort(key=lambda student: int(student[1]))

# 정렬된 이름 출력
print(*[student[0] for student in array])
