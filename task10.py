class Document:
    def __init__(self,title):
        self.title = title

    def print_preview(self):
        raise NotImplementedError("bu metod hali yozilmagan ")
    
class WordDocument(Document):
    def print_preview(self):
        return print(f"Word hujjat: {self.title}.doc - Tahrirlash ancxha qulay")
    
class PdfDocument(Document):
    def print_preview(self):
        return print(f"Pdf hujjat: {self.title}.pdf - O'qish uchin juda qulay")
    
word = WordDocument("sinf xona")
pdf = PdfDocument("hisobot")

word.print_preview()
pdf.print_preview()
