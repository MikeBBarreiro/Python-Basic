from stack import *


# Food goes into Self and 'hamburger' goes into name in the push function
# here in JS you would say
# var food = new Stack()
food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')

#Yumm... i just ate the cale, this pops 'cake, out the list'
food.pop()
