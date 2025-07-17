class Product:
    def __init__(self,title):
        self.title = title

    def get_delivery_method(self):
        raise NotImplementedError("get_delivery_metod hali yopzilmagan ")
    
    def download(self):
        raise NotImplementedError("downland metodi hali yozilmagan ")

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return print(f"{self.title} maxsulot uyga etkazib berilayapti")


class DigitalProduct(Product):
    
    def download(self):
        return print(f"{self.title} - Yuklab olishiga 5 soniya qoldi")
    

physical = PhysicalProduct("FasFood")
digital = DigitalProduct("eBook")

physical.get_delivery_method()
digital.download()


