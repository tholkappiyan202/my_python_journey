#legb 
#locally scoped varible , can be called and used onlyinside the same function , and is useless outside it
def name():
    my_name="tholkappiyan"
    print(my_name)
name()
 #print(my_name) #it is useless here

#enclosing scoped variable , a variable declared in outer (enclosing) function can be used in the inner function , but the opposite isn't possible
def outer():
    a ="thols"
    def inner():
        print(a)
        eg = 10
    inner()
outer()
#print(eg) is not possible because it is defined inside the inner function  i.e it is locally scopped
#globally scoped variable , they are defined outside all the functions , and  can be used everywhere , even inside the function 
age = 10 
dept = 'ece'
def sample():
    print(age)
    def sample2():
        print(dept)
    sample2()
sample()
