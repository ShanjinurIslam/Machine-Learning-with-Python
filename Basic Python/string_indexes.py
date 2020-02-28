selfish = 'spondon4'
#indexes   01234567 

print(selfish[0]) # prints first character in the string

# [start:stop]

print(selfish[0:3]) # start from 0 and end in 3-1 = 2

# [start:stop:stepover]

print(selfish[0:3:2]) # stepover = 2

print(selfish[::2])

# [-1] / index from the end here 8-2 = 6th index starting from 0
print(selfish[-2])

# reverses the string. very useful technique to reverse a string
var = selfish[::-1]
print(var)