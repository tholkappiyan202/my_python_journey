#actual example
class parent:
    def __init__(self):
        self.__data = "parent's data"
class child1(parent):
    def __init__(self):
        super().__init__() # here the parent's method is entered before the child . that is the child has inherited the parent's data 
        self.__data ="child's data" # here polymorphism , but with __ .the names are managed and not OVERIDDEN. the child's data is added along with parent's data due to SUPER.()
obj = child1()
print(obj.__dict__)
# it 's output is name mangling
