# 퀴즈
# from random import *
# users = range(1, 21)
# users = list(users)
# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4)
# print(winners)
# chickenWinner = sample(winners, 1)
# others = set(winners) - set(chickenWinner)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(chickenWinner))
# print("문상 당첨자 : {0}".format(others))

# weather = "비"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "눈":
#     print("우산을 챙기세요")
# else:
#     pass

# customer = "토르"
# person = "Unknown"
#
# while person != customer :
#     print('{0}, 커피가 준비되었습니다'.format(customer))
#     person = input("이름이 어떻게 되세요?")

# test = [1, 2, 3]
# for a in test:
#     print(a)

# test = {1: "a", 2: "b", 3: "c"}
# for k, v in test.items():
#     print(k, v)
#
# test = [1, 2, 3]
# for a in test:
#     print(a)

# for j in range(1, i):
#     print(k * j)
#
# for i in (1, 101):
#     if i % 15 == 0 :
#         print('FizzBuzz')
#     elif i % 3 == 0 :
#         print('Fizz')

# students = [1, 2, 3, 4]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# from random import randint
#
# drive_passengers = 0
# passengers = range(1, 51)
#
# for passenger in passengers:
#     drive_time = randint(5, 50)
#     if drive_time > 15:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(passenger, drive_time))
#     else:
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(passenger, drive_time))
#         drive_passengers += 1
# print("총 탑승 승객 : {0} 분".format(drive_passengers))

# def open_account():
#     print("새로운 계좌")
#
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money
#
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance
#
#
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
#
#
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
#
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}" \
#           .format(name, age, main_lang))
#
#
# profile(name="유재석", main_lang="파이썬", age=20)
# profile("김태호", 20, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}" \
#           .format(name, age, main_lang))
#
#
# profile("유재석")
# profile("김태호")
# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     # print([lang for lang in language])
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
#
# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
# profile("김태호", 20, "PHP", "C", "C++", "C#")
