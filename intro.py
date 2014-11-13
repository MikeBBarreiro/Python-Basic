#import math .. imports math!
import math

# this is a comment
# there are no var's in python just x = 3

x = 3
y = 4.2
z = 'hello'
a = 'world'

b = x + y

# in this the 3 is 3.0
ca = 8 / 3

# this does a floor and only show the interger
c = 8 // 3

# modules
e = 8 % 3

# 8 to the 3rd power
f = 8 ** 3

#this should say hellow world
g = z + a

# this is like console.log
print(x, y, z, a, b , c, ca, e, f, g)

# My First Function!
def volumeCylinder(r, h):
    return math.pi*(r**2)*h

a = volumeCylinder(4,8)
print('Volume Here-->', a)

#This takes a Binary Code and turns it into a decimal
def bin2Dec(str):
    sum = 0
    for index, bit in enumerate(str[::-1]):
        sum += int(bit) * (2**index)
    return sum

dec = bin2Dec('1001')
print(dec)
