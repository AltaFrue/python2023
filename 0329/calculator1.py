print("구구단 몇 단을 계산할까?")
ipt = input()
print("구구단", ipt, "단을 계산한다.")

for i in range(1, 10):
    result = int(ipt) * i
    print(ipt, " X ", i, " = ", result)