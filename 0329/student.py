print("당신이 태어난 연도를 입력하세요.")
myear = input()
myage = (2023 - int(myear)) +1

if myage >= 20 and myage <= 26:
    print("대학생")
elif myage < 20 and myage >= 17:
    print("고등학생")
elif myage < 17 and myage >= 14:
    print("중학생")
elif myage < 14 and myage >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")
