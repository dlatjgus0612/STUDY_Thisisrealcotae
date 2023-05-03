def func1():
  
  ##---수자료형---
  
  #실수의 소수부가 0일 때 생략
  a = 5.
  b = -.7
  print(a, b)
  
  ##지수표현방식
  #유효숫자e^지수 = 유효숫자X10^지수
  
  a = 3954e-3
  b = int(1e9)  #정수로 표현하고 싶으면
  print(a, b)
  
  #아무리 실수여도 미세오차가 있으니
  a = round(123.456, 2)  #둘째자리까지
  print(a)
  
  #연산자
  a = 5
  b = 3
  print(a % b, a // b, a**b, a**0.5)
  #나머지, 몫, 거듭 제곱, 제곱근
  
  ##---리스트자료형---
  #data를 연속적으로 처리하기 위해 like array, index = 0
  
  #indexing (접근)
  a = [1, 2, 3, 4, 5]
  print(a[2], a[-3])
  a[2] = 7
  print(a)
  
  #slicing
  print(a[1:4])
  
  #list comprehension
  #2차원 list에 효과적이다. 특히 N X M
  
  array = [i for i in range(20) if i % 2 == 1]  #0부터 19까지 중 홀수만 담기
  print(array)
  
  n = 4
  m = 3
  array = [['o'] * m for _ in range(n)]
  #언더바(_) : 반복을 위한 변수의 값 무시하고자
  print(array)
  array[1][2] = 7  #1행2열 변경확
  print(array)
  
  #관련 method들..
  
  #---문자열자료형---
  #concatenate and immutable
  print("Hello" + " " + "World")
  print("S" * 3)
  
  #tuple (또한 immutable)
  a = (1, 2, 3, 4, 5, 6)
  print(a[1:4])
  #for data관리, hashing, memory 효율적
  