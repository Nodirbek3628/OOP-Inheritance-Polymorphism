class Media:
    def __init__(self,author:str,time:int,name:str):
        self.author = author
        self.time:int = time 
        self.name = name

    def play(self):
        raise NotImplementedError("bu metod yozilmagan")
    
class Song(Media):
    def play(self):
        print(f"Author {self.author} time {self.time} is sings {self.name}") 

class Movie(Media):
    def play(self):
        print(f"Author {self.author} time {self.time} is movie name  {self.name}")
    
class Podcast(Media):
    def play(self):
        print(f"Author {self.author} time {self.time} podcast {self.name}")

song = Song("Shearali  ",105,"Uzbegim")
movie = Movie("Axad.Q",500,"Boy ota")
podcast = Podcast("Axad Xudayarov",240,"odob")


song.play()
movie.play()
podcast.play()