import random

output = ''
for i in range(7):
    for j in range(7):
        output += str(random.randrange(1, 49)) + ','
    output = output[:-1] + '\n'

print (output)