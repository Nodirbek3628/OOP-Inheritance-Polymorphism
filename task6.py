class Employe:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Hali funksiya yozilmgan ")
    
class Developer(Employe):
    def calculate_bonus(self):
       return self.salary * 0.15
    
class Manager(Employe):
    def calculate_bonus(self):
        return self.salary * 0.20
    
dev = Developer("Ali",1_400_000)
maneger = Manager("Vali",1_200_000)

print(f"Developer salary is bonnus {dev.calculate_bonus()}$")
print(f"Meneger salary is bonus  {maneger.calculate_bonus()}$")

