import datetime
class Name:
    
    class_attribute = " this is the end"
    def __init__(self,friends,enemy, habit1 , habit2):
        
        self.friends = friends 
        self.enemy= enemy
        self.habit1 = habit1
        self.habit2 = habit2
        
    def chat(self):
        good = print(f"im {self.friends} and \n my habit is {self.habit1.upper()} ")
        return good
    def spice(self):
        bad = print(f"im {self.enemy} and my habit is {self.habit2.lower()}")
    
name1 = Name("inba","hafiz","helping","bastard")
name1.chat()
print(Name.class_attribute)
print(name1.enemy)

variable=datetime.datetime.variable()
print(variable.strftime("%Y"))