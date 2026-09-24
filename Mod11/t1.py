class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, num_pages):
        super().__init__(name)
        self.author = author
        self.num_pages = num_pages
    
    def tulosta_tiedot(self):
        print(f"\nBook's name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Number of pages: {self.num_pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    
    def tulosta_tiedot(self):
        print(f"\nMagazine's name: {self.name}")
        print(f"Editor: {self.editor}")

book = Book('Hytti n:o 6', 'Rosa Liksom', 200)
mag = Magazine('Aku Ankka', 'Aki Hyyppä')

book.tulosta_tiedot()
mag.tulosta_tiedot()
