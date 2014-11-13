__author__='Michael'

#This makes a factory
class Stack:
    #internal data structure
    data= []
    # Instances Methods 
    def push(self, name):
        self.data.append(name)
    def pop(self, name):
        self.data.pop()

# Food goes into Self and 'hamburger' goes into name in the push function
# here in JS you would say
# var food = new Stack()
food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')

#Yumm... i just ate the cale, this pops 'cake, out the list'
food.pop()
