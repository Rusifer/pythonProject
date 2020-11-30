# 지역변수와 전역변수
# gun = 10
#
#
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내 ] 남은 총 : {0}".format(gun))
#
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내 ] 남은 총 : {0}".format(gun))
#     return gun
#
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
# def std_weight(height2, gender2):
#     height2 = height2 / 100
#     if gender2 == "남자":
#         weight2 = height2 * height2 * 22
#     else:
#         weight2 = height2 * height2 * 21
#     return weight2
#
#
# height = 175
# gender = "남자"
# weight = std_weight(height, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight, 2)))

# print('Java', 'Python', sep=',', end='?')
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)
#
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호 :" + str(num).zfill(3))

# input 으로 받은 값은 항상 string
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 {0} 입니다.". format(answer))

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0: >-10}".format(500))
print("{0:_<10}".format(500))
print("{0:,}".format(100000000000000))
print("{0:+,}".format(1000000000000000))
print("{0:+,}".format(-1000000000000000))
print("{0:^<+30,}".format(10000000000000))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
