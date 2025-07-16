class Media:
    def __init__(self,author):
        self.author = author

    def play(self):
        raise NotImplementedError("bu metod yozilmagan")
    
class Song(Media):
    def play(self):
        return 
    
