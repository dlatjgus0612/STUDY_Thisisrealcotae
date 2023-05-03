#사전자료형 O(n)
#key- value
#immutable

data = dict()
data['사과'] = "A"
data['바나나']="B"
data['코코넛']="C"
if '사과' in data:
  print("사과가 있네")

#key value 이용
key_list = data.keys()
value_list = data.values()
for key in key_list:
  print(data[key])

key_list = list(key_list)
print(key_list)

#집합자료형 O(1)
data = set([1,1,2,3,4,4,5]) #중복제거
print(data)
#연산
data.add(6)
data.update([7,8])
data.remove(4)
print(data)

#기본 입출력
print("기본입출력 실행. 개수 입력, 숫자입력 ")
n = int(input())
data = list(map(int, input().split())) #리스트, 함수적용, 정수로, 입력, 칸띄워서
data.sort(reverse=True) #내림차순정렬
print(data)

#빠르게 입력받기
print("빠르게 입력받기 실행")
import sys 
data = sys.stdin.readline().rstrip() #한줄데이터가 알아서 들어감
print(data)

print(3, end= " ") #공백후 바로 출력하기
print(4, end= " ")

#f-string 예제 _ 접두사 f로 문자열, 정수 함께 출력
answer = 7
print(f"정답은 {answer}입니다.")
