# 문제 20. 각 자릿수의 합 구하기

number = int(input())
hap = 0

for n in range(number+1) :
    hap += number % 10
    number = number // 10

print(hap)
