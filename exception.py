try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자: ")))
    nums.append(int(input("두 번째 숫자: ")))
    # nums.append(int(nums[0] / nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)