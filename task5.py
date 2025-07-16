class Appliance:
    def turn_on(self):
        print("Appliance turned on")

    def turn_off(self):
        print("Appliance turned off")


class TV(Appliance):
    def turn_on(self):
        print("TV: Efirga ulanmoqda...")

    def turn_off(self):
        print("TV: O'chdi, ekran qora.")


class Fridge(Appliance):
    def turn_on(self):
        print("Fridge: Sovutish boshlandi.")

    def turn_off(self):
        print("Fridge: Sovutish to'xtadi.")

tv = TV()
fridge = Fridge()

devices = [tv, fridge]

for device in devices:
    device.turn_on()
    device.turn_off()
