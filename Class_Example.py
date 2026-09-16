class Person:
    def __init__(self,name,age,weight,height,address,gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.address = address
        self.gender = gender
    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}\nWeight = {self.weight}\nHeight = {self.height}\nAddress = {self.address}\nGender = {self.gender}"
    def warrior(self):
        self.weight = self.weight * 1.5
        self.height = self.height * 1.2
        return self.weight,self.height


Hot = Person("Hot",19,51,175,"Chaiyapoom","Male")
print(Hot)
Hot.warrior()
print(Hot)