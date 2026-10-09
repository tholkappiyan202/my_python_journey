#tuple syntax: tuple = ("value1" , value2)
#can be accessed by index
#cannot be modified (  gives TypeError)
sample= "tholkappiyan"
sample_tuple = tuple(sample)
print(sample_tuple)
# they can be SPLICED like lists ,based on index
desserts = ('cake', 'pie', 'cookies', 'ice cream','pie')
print(desserts[1:3:1]) 
print('cake' in desserts)

print(desserts.count('pie'))

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse = True))

