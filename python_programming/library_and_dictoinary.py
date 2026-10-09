data = ['thols','kannagi', 'amma', 'thaatha']
def long_name(spoon):
    return len(spoon)>2
result = tuple(filter(long_name,data))
print(result)

import datetime
eg = datetime.date(2026,6,15)
print(eg.year)
print(eg.month)
# import re module

import re
name_variable = " the name is thols710"
print(re.search("7\d+",name_variable,))

# all operator
sample = ["one","two"]
print(all( isinstance(i,str) for i in sample))