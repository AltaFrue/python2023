import random

def calc(x):
    print("구구단 ", str(x), "단을 계산합니다.")
    for i in range(1, 10):
        print(str(x), "x", str(i), "=", str(x*i))

def rand():
    guess_number = random.randint(1, 100)
    print("숫자를 맞혀 보세요. (1 ~ 100)")
    users_input = int(input())
    while (users_input is not guess_number):
        if users_input > guess_number:
            print("숫자가 너무 큽니다.")
        else:
            print("숫자가 너무 작습니다.")
        users_input = int(input())
    else:
        print("정답입니다.", "입력한 숫자는", users_input, "입니다.")

def main():
    while True:
        print("**********************")
        print("* 1. 구구단 출력     *")
        print("* 2. 숫자 찾기 게임  *")
        print("* 0. 종료            *")
        print("**********************")
        game = int(input("숫자를 입력하세요: "))

        if game == 1:
            c = int(input("단을 입력하세요 :"))
            calc(c)
        if game == 2:
            rand()
        if game == 0:
            break
        else:
            print("0,1,2의 숫자중 하나를 입력하세요.")
    print("게임이 끝났습니다!")

if __name__=='__main__':
     main()