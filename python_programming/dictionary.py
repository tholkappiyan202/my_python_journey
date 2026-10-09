products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for inde , variable in enumerate(products.values() ,1):
    print(inde ,variable)

#updation
for key,value in products.items():
    products[key] = round(value*0.5)
    
print(products)

#sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 6}
print(set1.add(6))
print(set1.issubset(set2))
print(set2.issuperset(set1))
set1.discard(2)
print(set1)
set1 ^= set2 #set1 got updated
print(set1)
print(4 in set2)