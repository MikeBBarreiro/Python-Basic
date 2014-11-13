#This makes a factory
class Stack:
    #internal data structure
    data= []
    # Instances Methods
    def push(self, name):
        self.data.append(name)
    def pop(self, name):
        self.data.pop()
