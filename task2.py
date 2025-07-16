class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
        
    def show_Info(self):
        print(f"{self.brand} {self.model}")

class Car(Vehicle):
    def show_Info(self): 
        print(f"{self.brand} {self.model} 4 g'ildirakli tez va qulay")
        
class Bike(Vehicle):
    def show_Info(self):
        print(f"{self.brand} {self.model} 2 g'ildirakli bez rasxod ")

    
car = Car("chevrolet","gintra ") 
bike  = Bike("aise","R15")   

car.show_Info()
bike.show_Info()
