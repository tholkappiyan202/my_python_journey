#list() is used to convert a string into a list
sample= "tholkappiyan"
sample_list = list(sample)
print(sample_list)

#general list and the accessing is by using the zero based indexing
the_list = ["name", "standard" ,  "age" , "songs" , 19]
length = len(the_list)
print(length)
the_list[0] = "tholkappiyan"
del(the_list[2])
print(the_list)
# we can also check if specific elements are present in the list using "in " operator
print("standard" in the_list)

# nested lists
nest = [ "name" , [15 , 'thols' , 49]]
print(nest[1][2])
# unpacking the list  is starting from zero index . it is assigning VARIABLES to the values in the list
zero ,  *remaining = nest 
print(zero,remaining)

# list operations
#(1 append : attaches the list to the other list , even seperate elements
list1 = ["hello", 0 , 1 , 12 , 45,12,12]
list2 = [" hi", 5 , 6 , 7 ,8]
list3 = [False , 8 , 5 , 4,4,8,9,4,4 ]
list1.append(list2)
print(list1)

#2 extend : extends the first list and puts all the elements of the second list
list2.extend(list3)
print(list2)
#3 insert synatx :  list.insert(index ,value)
list3.insert(1 , True)
print(list3)
#4 remove : syntax(value) , this finds the index and removes the element . 
# if more of the same elements are present only one element is removed, the remaining are present
list3.remove(4)
print(list3)

#5 pop() ,:  syntax : list.pop(index) removes the  element present in the given INDEX
#if no idex is given ( i.e pop()) then it moves the last element
list3.pop(1)
print(list3)


#6 clear() ,: syntax :  clear() //clears the entire list
list2.clear()
print(list2)
#6 sort() , syntax :  list.sort()  , arranges in the ascending order and modifies the original string
list3.sort()
print(list3)
#7 . sorted() , syntax :  sorts in ascending order and stroes it in new variable , the original remains same
# // it cannot sort STRINGS  but BOOL are sorted
sorted_list = sorted(list3)
print(sorted_list)

#8  reverse()  , syntax :  list.reverse()
list3.reverse()
print(list3)

#9 index() , syntax: list.index(value) // finds the index of the entered value
index = list3.index(5)
print(index)
# we can specify it from where to start searching for the entered value and where to end
# count : syntax:  list.count("value") , returns the no of times the value is present
print(list3.count(4))

#10 . len . counts the no of elements in the list . if i want to find a particular item's count , use list.count("needed")
print(len(list1))