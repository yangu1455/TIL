# 주석처리 된 코드가 문제 
# 주석처리 안 된 코드가 내가 수정한 코드


# 예제 03. [오류 해결] 입력 받기

# numbers = input().split()
# print(sum(numbers))

# 기본적으로 input()은 문자열로 받아오기 때문에 두 수를 숫자로 받으려면 형변환을 해줘야한다.

numbers = map(int, input().split())
print(sum(numbers))




# 예제 04. [오류 해결] 입력 받기 - 2

# words = list(map(int, input().split()))
# print(words)

# 문자열을 입력받기 위해서는 형변환을 해주면 안되고, split()으로 나눠준 것은 기본적으로 값이 리스트로 나온다.

words = input().split()
print(words)




# 예제 05. [오류 해결] 숫자의 길이 구하기

# number = 22020718
# print(len(number))

# len() 함수를 사용하기 위해서는 str로 형변환을 해주어야한다.

number = str(22020718)
print(len(number))