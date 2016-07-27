1. Stack
//List Stack
class ListStack:
    # Init
    def __init__(self):
        self._theItems = list()

    # Length
    def __len__(self):
        return len(self._theItems)

    # IsEmpty
    def isEmpty(self):
        return len(self._theItems) == 0

    # Push
    def push(self, item):
        self._theItems.append(item)

    # Pop
    def pop(self):
        assert not self.isEmpty(), "Pop cannot be done at an empty Stack."
        self._theItems.pop()

    # Peek
    def peek(self):
        assert not self.isEmpty(), "Pop cannot be done at an empty Stack."
        return self._theItems[-1]

    # Iter
    def __iter__(self):
        return _StackIter(self._theItems)

class _StackIter:
    # Init
    def __init__(self, theItems):
        self._theItems = theItems
        self._size = 0
    def __iter__(self):
        return self
    def next(self):
        if self._size < len(self._theItems):
            cItem = self._theItems[self._size]
            self._size += 1
            return cItem
        else:
            raise StopIteration

def test_liststack():
    
    print '#Init a stack named smith using push'
    smith = ListStack()
    smith.push('CSCI-112')
    smith.push('MATH-121')
    smith.push('HIST-340')
    smith.push('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#pop one item'
    smith.pop()
    
    print '\n#output smith stack after pop'
    for element in smith:
        print element 
        
    print '\n#get the peek item'
    peek_item = smith.peek()
    print 'peek item is ', peek_item
    
    print '\n#get the length of stack'
    print 'the lenght of stack is ', len(smith)
    
    print '\n#check wheter the stack is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#pop all items'
    while not smith.isEmpty():
        smith.pop()
    
    print '\n#check wheter the stack is empty after pop all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_liststack()

//LinkedList Stack
class LinkListStack:
    # Init
    def __init__(self):
        self._top = None
        self._size = 0

    # Length
    def __len__(self):
        return self._size

    # IsEmpty
    def isEmpty(self):
        return self._size == 0

    # Push
    def push(self, item):
        if self._top is None:
            newNode = _StackNode(item)
            newNode.next = None
            self._top = newNode
            self._size += 1
        else:
            newNode = _StackNode(item)
            newNode.next = self._top
            self._top = newNode
            self._size += 1

    # Pop
    def pop(self):
        assert not self.isEmpty(), "Stack is empty."
        self._top = self._top.next
        self._size -= 1

    # Peek
    def peek(self):
        assert not self.isEmpty(), "Stack is empty."
        return self._top.item

    # Iter
    def __iter__(self):
        return _StackIter(self._top)

class _StackNode:
    # Init
    def __init__(self, theItem):
        self.item = theItem
        self.next = None

class _StackIter:
    # Init
    def __init__(self, top):
        self._cTop = top
    def __iter__(self):
        return self
    def next(self):
        if self._cTop is not None:
            item = self._cTop.item
            self._cTop = self._cTop.next
            return item
        else:
            raise StopIteration

def test_linkliststack():
    
    print '#Init a stack named smith using push'
    smith = LinkListStack()
    smith.push('CSCI-112')
    smith.push('MATH-121')
    smith.push('HIST-340')
    smith.push('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#pop one item'
    smith.pop()
    
    print '\n#output smith stack after pop'
    for element in smith:
        print element 
        
    print '\n#get the peek item'
    peek_item = smith.peek()
    print 'peek item is ', peek_item
    
    print '\n#get the length of stack'
    print 'the lenght of stack is ', len(smith)
    
    print '\n#check wheter the stack is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#pop all items'
    while not smith.isEmpty():
        smith.pop()
    
    print '\n#check wheter the stack is empty after pop all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_linkliststack()
