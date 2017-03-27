from singleLinkeList import SingleLinkedList as LinkedList

class Stack:
    def __init__(self):
        self._items = LinkedList()

    def __len__(self):
        return len(self._items)

    def isEmpty(self):
        return self._items.listIsEmpty()

    def pop(self):
        self._items.listNodeDelete(-1)

    def push(self, item):
        if self.isEmpty():
            self._items.listNodeInsert(item, 0)
        else:
            self._items.listNodeInsert(item, -1)
        
    def top(self):
        return self._items[-1]

def testStack():
    
    myStack = Stack()
    print myStack.isEmpty()
    
    myStack.push(1)
    myStack.push(3)
    myStack.push(5)

    for item in myStack._items:
        print item, 
        
    print '\r'
    print myStack.top()
    myStack.pop()
    for item in myStack._items:
        print item, 
        
    print '\r'
    myStack.pop()
    myStack.pop()
    print myStack.isEmpty()

'''
True
1 3 5 
1
1 3 
True
'''        
if __name__ == "__main__":
    testStack()
