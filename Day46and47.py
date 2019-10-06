#task1
class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

class science_section(Library):
    def __init__(self, book, shelf, name):
        super().__init__(book, shelf)
        self.name = name

#science = science_section(self)
    def sc(self):
        print(self.book, self.shelf, self.name)

i = science_section(45, 300, "Physics books")
i.sc()
i.book = 20
i.shelf = 4
i.sc()


