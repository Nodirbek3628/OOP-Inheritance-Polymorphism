class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def slep(self):
        print(f"{self.name} is sleping")

    def run(self):
        print(f"{self.name} is runing ")

    def eats(self):
        print(f"{self.name} is eating")

    def speak(self):
         print(f"{self.name} makes a sound")
    
class Dog(Animal):

    def fetch(self):
        print(f"{self.name} is fetch")
    
    def speak(self):
        print(f"{self.name} says Woof ")

class Cat(Animal):

    def sheerring(self):
        print(f"{self.name} is sheerring")

    def speak(self):
        print(f"{self.name} says Meow ")


dog = Dog("Simba",5)
cat = Cat("Tom",6)


dog.fetch()
dog.speak()
cat.sheerring()
cat.speak()

