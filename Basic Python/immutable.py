var = 'Spondon'

# var[0] = 's' -> python strings are immutable that means it does not support item assignment

# the only way to change this to reassign it 

# to make var = 'spondon'
var = 's' + var[1:]

print(var)