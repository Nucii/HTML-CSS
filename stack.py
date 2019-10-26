class Stack:
    def __init__(self):
        self.myStack = []
        

    def PushItem(self, val):
        self.myStack.append(val)

    def PopItem(self, val):
        return self.myStack.remove()

    def ViewItems(self):
        return self.myStack


myStack = Stack()
myStack.PushItem(1)
myStack.PushItem(2)
print(myStack.ViewItems())
