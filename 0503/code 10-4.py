class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def about_me(self):
        print("저의 이름은", self.name, "이고요, 제 나이는", str(self.age), "살입니다.")

print("52383013 CHOI RAK HUN")