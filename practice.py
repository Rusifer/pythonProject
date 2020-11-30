# print("나는 {} 살입니다.".format(20))
#
# print("나는 {}색과 {}색을 좋아해요".format("파란", "발간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "발간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))
#
# age = 29
# color = "Red"
# print(f"나는 {age}살이고, {color}색을 좋아해요")

# print("백문이 불여일견\r\n백견이 불여일타")
# print("저는 \"ssg\"입니다")
# print("\\dd\b\ts")

# url = "http://naver.com"
#
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(password)
#
# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 2))
# print(min(5, 12))
# print(round(3.14))
#
# import math
# print(math.floor(4.99))
#
# from random import *
# print(random())
# print(int(random() * 10) + 1)
#
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
#
# print(randrange(1, 46))
#
# print(randint(1, 45))

# from random import *
# day = randint(4, 28)
#
# day = randrange(4, 29)

# 리스트 [] : 순서를 가지는 객체의 집합
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# 조세호가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# 하하가 다음 정류장에서 탐
# subway.append("하하")
# print(subway)

# 정형돈을 유재석 / 조세호 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# subway.pop()
# print(subway)

# 같은 사람이 몇 명 있는가
# subway.append("유재석")
# print(subway.count("유재석"))

# 하나 삭제
# subway.remove("유재석")
# print(subway)

# 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()

# 다양한 자료형 사용가능
# num_list = [1, 2, 3, 4, 5]
# mix_list = ["조세호", 20, True]
#
# mix_list.extend(num_list)
# print(mix_list)

# 사전 (Dictionary) : 해쉬

# cabinet = {"1":"유재석", "2":"김태호"}
# print(cabinet["1"])
# del cabinet["2"]
# cabinet["3"] = "양세찬"
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
# print(cabinet.get("1"))
# print(cabinet.get("4", "없음"))

# 튜플 : 상수 변경불가
# menu = ("돈까스", "치츠까스")
# print(menu[0])

# name = "김종국"
# age = "40"
# hobby = "헬쓰"

# (name, age, hobby) = ("김종국", 40, "헬쓰")
# print(name, age, hobby)

# 집합(set) : 중복안됨, 순서없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세찬"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 값 추가 삭제
python.add("김태호")
print(python)
java.remove("김태호")
print((java))

java.update(["양세형", "송지효"])
print(java)


