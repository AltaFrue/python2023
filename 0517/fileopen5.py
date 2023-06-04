with open("d:\CRH\python\\0517\\dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")

print("총 글자의 수:", len(contents))
print("총 단어의 수:", len(word_list))
print("총 줄의 수:", len(line_list))
