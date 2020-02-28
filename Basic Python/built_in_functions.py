var = 'My name is Spondon'

print(var.upper())
print(var.lower())
print(var.split())
# print(type(var.split())) -> List

print(var.find('is')) # returns index
print(var.replace('name','Name'))

var = 'My age is {}'
print(var.format(24))