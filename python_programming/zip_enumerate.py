#enumerate(variable) gives the output with the index number along with the value of the variable
fruits = [ 'apple' , 'orange', 'banana', 'grape']
print(list(enumerate(fruits)) )


#zip(variable1 , variable2) :  combines two variales side by side
app = ['insta', 'whatsapp', 'facebook']
user = [ 'gokul', 'kanish', 'arjun']
print(list(zip(app,user)))


for variable in fruits:
    print(f"the fruit is { variable}")
  
for index,variable1 in enumerate(fruits,0):
    print(f"the no {index} fruit is {variable1}")
    
    
for var1 , var2 in zip(app, user):
    print(f"the app is {var1}")
    print(f"the user is {var2}")
    
odd = [same for same in range(30) if same %2 !=0 ]
print(odd)

numbers = [0,1, 2 , 3 , 4 ,5 ]

comprehension = [(num, 'odd') if num % 2  != 0 else (num, 'even')  for num in numbers  ]
print(comprehension)

#filter(list , funtion
data = ['thols','kannagi', 'amma', 'thaatha']
def long_name(vari):
    return len(vari)>5
result = list(filter(long_name,data))
print(result)
 #map(function , data)
#it applies the function each value INDIVIDUALLYY unlike the filter which gives the whole value to the function 
data1 = {1,3,4,5,6,7,8}
def odd_even(vari2) :
   if vari2%2 == 0  :
    return("it is even")
   else:
       return "it is odd"
print(list(map(odd_even,data1)))

print(sum(data1,start=10))

#lambda funtion ( useful for one line functions )
print(tuple(map(lambda var:  var ** 3 ,  data1)))