class yt:
    def __init__(self,content):
        self.content = content
    def video(self):
        return f"{self.content} is posted"
class fb:
    def __init__(self,content):
        self.content = content
    def video(self):
        return f"{self.content} is for boomers !!!"
class ig:
    def __init__(self,content):
        self.content = content
    def video(self):
        return f"{self.content} is pakka brain rot !!"
    
def common(uploaded_content):
    print(uploaded_content.video())
    
post = yt("mr.beast")
article = fb("prakasam sir's content")
story = ig("shakil's reels feed")

print(story.video())
                
common(post)
common(story)
common(article)

#inheritance polymorohism 
#in normal polymorphism , the different classes are not child . if they are child(inheritance) and have the same method(polymorphism),they can be accessed like inheritance

class Animal:
    def speak(self):
        return 'Some generic sound'

class Cat(Animal):
    def speak(self):
        return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'
animals = [Cat(),Dog(),Monkey()]
for animal in animals:
    print(animal.speak())
  
print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak()) # Some generic sound
