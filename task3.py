class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def acces_level(self):
        print("Admin vs Guest")

class Admin(User):
    def acces_level(self):
        print(f"Mening ismim {self.name} yoshim {self.age}da bizning Oquv markazga xush kelibsz")

class Guest(User):
    def acces_level(self):
        print(f"ismim {self.name} yoshim {self.age}da Kurslar tulovlari qancga")


admin = Admin("shaxa",25)
guest = Guest("ali",35)

admin.acces_level()
guest.acces_level()