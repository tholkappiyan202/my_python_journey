from abc import ABC , abstractmethod

class ANIMNAL(ABC): # it inherits from the ABC
    def sample(self):
        pass

class DOG(ANIMNAL): # concrete class one
    def sample(self):
        print("bow bow")
    
class CAT(ANIMNAL):
    def sample(self):
        print( "meow")
class MONKEY(ANIMNAL):
    def sample(self):
        print("heheh ! \n")
        
list1 = [DOG(), CAT() , MONKEY()]
print(DOG().sample())

for list2 in list1 :
    list2.sample()
    
    #example from the website
from abc import ABC, abstractmethod

# The blueprint for any toy that can speak
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()