import os
import random, datetime

if not os.path.isdir("log"):
    os.mkdir("log")

if not os.path.exists("log/abc.txt"):
    f = open("abc.txt", "w", encoding="utf8")
    f.write("기록이 시작된다.\n")
    f.close()


while True:
    print("***************************************")
    print(" 1. 파일 추가       2. 파일 삭제       ")
    print(" 3. 종료                               ")
    print("***************************************")
    calc = int(input("원하는 메뉴를 선택하세요:"))

    if calc == 1:
        with open("log/abc.txt", "a", encoding="utf8") as f:
            stamp = str(datetime.datetime.now())
            value = str(input("내용을 입력하세요: "))
            log_line = stamp + "\t" + str(value) + "\n"
            f.write(log_line)
            f.close()

    if calc == 2:
        with open("log/abc.txt", "w", encoding="utf8") as f:
            f.close()
    if calc == 3:
        break

print("Good Bye~~")
