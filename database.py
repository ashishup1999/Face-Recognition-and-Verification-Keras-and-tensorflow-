class database:
    def __init__(self):
        self.db=None
        
    def create_db(self):
        self.db={}

    def insert_db(self,enc):
        print("enter the name :")
        name=input()
        self.db[name]=enc
        
