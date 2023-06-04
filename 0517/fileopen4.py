with open("d:\CRH\python\\0517\\dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i) + " === " + line.replace("\n", ""))
        i = i + 1
