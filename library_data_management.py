class LibraryItem:
    def __init__(self,id,title,year):
        self.__id=id
        self.title=title
        self.year=year
        
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.title
    def get_year(self):
        return self.year
        
class Book(LibraryItem):
    def __init__(self, id, title, year,author):
        super().__init__(id, title, year)
        self.author=author
        
    def get_author(self):
        return self.author
    
        
class Magazine(LibraryItem):
    def __init__(self, id, title, year,issue):
        super().__init__(id, title, year)
        self.issue=issue
        
    def get_issue(self):
        return self.issue
    
    
Book_details=Book(1,"My Care Taker",2018,"Scott")
print("Id: ",Book_details.get_id())
print("Title: ",Book_details.get_title())
print("Year: ",Book_details.get_year())
print("Author: ",Book_details.get_author())

Magazine_details=Magazine(5,"Petty India",2022,5)
print("Id: ",Magazine_details.get_id())
print("Title: ",Magazine_details.get_title())
print("Year: ",Magazine_details.get_year())
print("Issue: ",Magazine_details.get_issue())
        

    