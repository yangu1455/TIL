# 주석처리 된 코드가 문제 
# 주석처리 안 된 코드가 내가 수정한 코드


# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기


# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)


# append 함수를 써서 값을 저장하기 위해서는 answer가 튜플이 아닌 list여야한다.

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)



# 예제 07. [오류 해결] 평균 구하기


# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)


# for 문 안으로 count += 1 들여쓰기가 되어야하고 // 는 소수점을 뗀 정수만을 돌려주기때문에 원하는 도출값을 위해 / 하나만 써야한다.


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)



# 예제 08. [오류 해결] 모음의 개수 찾기


# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)


# if 문 조건에서 그냥 “문자”는 True 값을 나타낸다.
# 따라서 char == 를 전부 붙여주어야 원하는 값이 도출된다.


word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)




# 예제 09. [오류 해결] 과일 개수 구하기


# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)


# fruit_count = {fruit: 1} 라는 코드 때문에 fruit_count 라는 리스트가 매번 키와 값이 한쌍인 딕셔너리로 초기화 된다.


from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)