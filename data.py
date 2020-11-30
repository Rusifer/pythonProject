# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# print(profile)
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import  pickle
# text_file = open("abc.txt", "r")
# text_list = text_file.readlines()
# with open("abc.bin", "wb") as file:
#     pickle.dump(text_list, file)
# text_file.close()
#
# with open("abc.bin", "rb") as file:
#     data = pickle.load(file)
# print(data)
# with open("study.txt", "w", encoding="utf8") as file:
#     print(file.write("파이썬을 열심히 공부하고 있어요"))
#
# with open("study.txt", "r", encoding="utf8") as file:
#     print(file.read(file))

for data in range(1, 51):
    file_name = str(data) + "주차.txt"
    with open(file_name, "w", encoding="utf8") as report_file
        report_file.write(" - {0} 주차 주간보고 -".format(data))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무요약 :")



