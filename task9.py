class Notification:
    def __init__(self,name):
        self.name = name

    def send(self):
        raise NotImplementedError("bu metod hali yozilmagan ")
    
class EmailNotification(Notification):
    def send(self):
         print(f"EmailNotification {self.name}@gmail.com")

class SmsNotification(Notification):
    def send(self):
        print(f"SmsNotification came  {self.name}")

email = EmailNotification("ali")
sms = SmsNotification("vali")

email.send()
sms.send()
