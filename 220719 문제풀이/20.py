# 문제 20. 각 자릿수의 합 구하기

number = int(input())
hap = 0

for n in range(number+1) :
    hap += number % 10
    number = number // 10

print(hap)


# 강사님 코드 1


number = 123
result = 0

while number:
    result += number % 10
    number //= 10

print(result)


# 강사님 코드 2

number = 123
result = 0

while number:
    # divmod(x, y)는 x를 y로 나누고, 
    # 결과를 tuple로 반환 
    # (몫, 나머지)
    number, remainder = divmod(number,10)
    result += remainder

print(result)