# 문제 21. 숫자 뒤집기

number = input()
rev = list(number)
rev.reverse()

print(''.join(rev))


# 강사님 코드

number = 123

result = 0
while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number % 10
    # number를 깎는다.
    number //= 10

print(result)