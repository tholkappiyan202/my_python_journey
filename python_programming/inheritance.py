class animal:
    def __init__(self,name):
        self.name =name 
    def sound(self):
        return f"{self.name}'s makes a sound "
class mammal(animal):
    bark = "woow" # this is a class attribute , meaining it can be used anywhere in this class
    def sound(self):
        base  = super().sound()
        return f"here {base} woke up , {self.name} made the sound'{self.bark}"
    
ani1= mammal("blacky")
ani2 = mammal("whitey")
print(ani1.sound())
print(ani2.sound())
print(ani2.bark)

