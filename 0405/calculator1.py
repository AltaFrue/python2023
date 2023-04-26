def f_plus(x ,y):
    print("결과:", x + y)

def f_minus(x, y):
    print("결과:",x - y)

def f_multi(x, y):
    print("결과:",x * y)

def f_division(x, y):
    print("결과:",x / y)

def f_sum(x, y):
    result = (x + y) * (max(x,y) - min(x,y) + 1) // 2
    print("결과:", result)

def f_max(x, y):
    lst = [x, y]
    print("결과:",max(lst))

def f_aa(x, y):
    print("결과:",str(x) + str(y))

def main():
    while True:
        print("*****************************")
        print(" 1. 더하기      2. 빼기       ")
        print(" 3. 곱하기      4. 나누기     ")
        print(" 5. 합산        6. Max값 찾기 ")
        print(" 7. 문자열결합  8. 종료      ")
        print("*****************************")
        calc = int(input("숫자를 입력하세요: "))

        if calc == 1:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_plus(b, c)            
        if calc == 2:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_minus(b, c)
        if calc == 3:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_multi(b, c)
        if calc == 4:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_division(b, c)
        if calc == 5:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_sum(b, c)
        if calc == 6:
            b = int(input("x 값을 입력하세요: "))
            c = int(input("y 값을 입력하세요: "))
            f_max(b, c)
        if calc == 7:
            b = str(input("x 값을 입력하세요: "))
            c = str(input("y 값을 입력하세요: "))
            f_aa(b, c)
        if calc == 8:
            break
        else:
            print("위 숫자중 하나를 입력하세요.")
    print("계산이 끝났습니다!")

if __name__=='__main__':
     main()
"""
for i in range(1,10):
    print('*'*i)

for i in range(1,10):
    print(' '*(10-i) + '*'*n)

for i in range(1,10):
    print(' '*(10 - i) + '*'*(2*i - 1)) """