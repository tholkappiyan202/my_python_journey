class Cat: # class ClassName
    def __init__(self, name , age,sound ): #
        self.name = name 
        self.age = age
        self.sound =sound
    def talk(self):
        a=print(f"im {self.name} and im {self.age} years old  ")
        return a
    def bark(self):
        b= print(f"im {self.name} and my sound is {self.sound}" )
        return b
cat_1 = Cat("kitty",2,'bow')
cat_2 = Cat("pussy cat", 3, 'meow')
print(cat_2.sound)
# calling the created ojects
cat_1.talk()
cat_2.talk()
cat_1.bark()
cat_2.bark()
print(cat_2.sound)
print(getattr(cat_1,"age","default"))
class PERSON:
    def __init__(self,pokemon,type):
        self.pokemon = pokemon
        self.type = type
user1 = PERSON("charizard",'fire')
user2 = PERSON("blastoise", "water")
print(user1.pokemon)
print(user1.type)
print(getattr(user1,"type",4))



import datetime 
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d")) 