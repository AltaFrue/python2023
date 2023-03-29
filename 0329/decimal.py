print("10진수를 입력하세요.")
decimal = int(input())
result = ' '
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(result)