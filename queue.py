# ListStack
class ListQueue:
    # Init
    def __init__(self):
        self._theItems = list()

    # Length
    def __len__(self):
        return len(self._theItems)

    # IsEmpty
    def isEmpty(self):
        return len(self._theItems) == 0

    # Enqueue
    def enqueue(self, item):
        self._theItems.append(item)

    # Dequeue
    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty."
        self._theItems.pop(0)

    # Iter
    def __iter__(self):
        return _QueueIter(self._theItems)

class _QueueIter:
    # Init
    def __init__(self, theItems):
        self._theItems = theItems
        self._count = 0
    def __iter__(self):
        return self
    def next(self):
        if self._count < len(self._theItems):
            theItem = self._theItems[self._count]
            self._count += 1
            return theItem
        else:
            raise StopIteration

def test_listqueue():
      
    print '#Init a queue named smith using enqueue'
    smith = ListQueue()
    smith.enqueue('CSCI-112')
    smith.enqueue('MATH-121')
    smith.enqueue('HIST-340')
    smith.enqueue('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#dequeue one item'
    smith.dequeue()
    
    print '\n#output smith after dequeue'
    for element in smith:
        print element 
        
    print '\n#get the length of queue'
    print 'the lenght of queue is ', len(smith)
    
    print '\n#check wheter the queue is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#dequeue all items'
    while not smith.isEmpty():
        smith.dequeue()
    
    print '\n#check wheter the queue is empty after dequeue all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_listqueue()
    
# LinkList Queue
class LinkListQueue:
    # Init
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        newNode = _QueueNode(item)
        if self.isEmpty():
            self._front  = newNode
            self._back = newNode
            self._size += 1
        else:
            self._back.next = newNode
            self._back = newNode
            self._size += 1

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty!"
        if self._front == self._back:
            node = self._front.value
            self._front = None
            self._back = None
            self._size -= 1
        else:
            node = self._front.value
            self._front = self._front.next
            self._size -= 1

    def __iter__(self):
        return _QueueIter(self._front)

class _QueueNode:
    # Init
    def __init__(self, item):
        self.value = item
        self.next = None

class _QueueIter:
    # Init
    def __init__(self, front):
        self._front = front
    def __iter__(self):
        return self
    def next(self):
        if self._front is not None:
            node = self._front.value
            self._front = self._front.next
            return node
        else:
            raise StopIteration

def test_linklistqueue():
      
    print '#Init a queue named smith using enqueue'
    smith = LinkListQueue()
    smith.enqueue('CSCI-112')
    smith.enqueue('MATH-121')
    smith.enqueue('HIST-340')
    smith.enqueue('ECON-101')
    
    print '\n#output smith stack'
    for element in smith:
        print element
           
    print '\n#dequeue one item'
    smith.dequeue()
    
    print '\n#output smith after dequeue'
    for element in smith:
        print element 
        
    print '\n#get the length of queue'
    print 'the lenght of queue is ', len(smith)
    
    print '\n#check wheter the queue is empty'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
        
    print '\n#dequeue all items'
    while not smith.isEmpty():
        smith.dequeue()
    
    print '\n#check wheter the queue is empty after dequeue all items'
    if smith.isEmpty():
        print 'stack is empty!'
    else:
        print 'stack is not empty!'
    
if __name__ == "__main__":
    test_linklistqueue()
    
# Array Queue
import ctypes

class Array:
    # Init
    def __init__(self, size):
        assert size > 0, "size should be above than 0"

        PyObjects = ctypes.py_object * size
        self.slots = PyObjects()
        self.size = size
        self.clear(None)

    # Len
    def __len__(self):
        return self.size

    # Get item
    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        return self.slots[index]

    # Set item
    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size, "index must be within the valid range."

        self.slots[index] = value

    # Clear
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    # Iterator
    def __iter__(self):
        return ArrayIterator(self.slots)

class ArrayIterator:
    # Init
    def __init__(self, slots):
        self.slots = slots
        self.index = 0
    # Iter
    def __iter__(self):
        return self
    # Next
    def next(self):
        if self.index < len(self.slots):
            item = self.slots[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

class ArrayQueue:
    # Init
    def __init__(self, maxSize):
        self._front = 0
        self._back = maxSize - 1
        self._size = 0
        self._qArray = Array(maxSize)

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return len(self._qArray) == self._size

    def enqueue(self, item):
        assert not self.isFull(), "Queue is full."
        maxSize = len(self._qArray)
        self._back = (self._back+1)%maxSize
        self._qArray[self._back] = item 
        self._size += 1

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty."
        maxSize = len(self._qArray)
        node = self._qArray[self._front]
        self._front = (self._front+1)%maxSize
        self._size -= 1
        return node

    def __iter__(self):
        return _QueueIter(self._qArray, self._front, self._size)

class _QueueIter:
    # Init
    def __init__(self, qArray, front, size):
        self._qArray = qArray
        self._front = front
        self._size = size
        self._index = 0
    def __iter__(self):
        return self
    def next(self):
        if self._index < self._size:
            node = self._qArray[self._front]
            self._front = (self._front+1)%len(self._qArray)
            self._index += 1
            return node
        else:
            raise StopIteration

def test_arryqueue():
    
    print '#Init a queue named smith using enqueue'
    smith = ArrayQueue(4)
    smith.enqueue('CSCI-112')
    smith.enqueue('MATH-121')
    smith.enqueue('HIST-340')
    smith.enqueue('ECON-101')
    
    print '\n#output smith queue'
    for element in smith:
        print element
           
    print '\n#dequeue one item'
    smith.dequeue()
  
    print '\n#output smith after dequeue'
    for element in smith:
        print element 
        
    smith.enqueue('ECON-102')  
    print '\n#output smith after enqueue again'
    for element in smith:
        print element 
        
    print '\n#get the length of queue'
    print 'the lenght of queue is ', len(smith)
    
    print '\n#check wheter the queue is empty'
    if smith.isEmpty():
        print 'queue is empty!'
    else:
        print 'queue is not empty!'
        
    print '\n#dequeue all items'
    while not smith.isEmpty():
        smith.dequeue()
    
    print '\n#check wheter the queue is empty after dequeue all items'
    if smith.isEmpty():
        print 'queue is empty!'
    else:
        print 'queue is not empty!'
        
    print '\n#init again'
    smith.enqueue('CSCI-112')
    smith.enqueue('MATH-121')
    smith.enqueue('HIST-340')
    smith.enqueue('ECON-101')
    
    print '\n#output smith queue'
    for element in smith:
        print element
    
if __name__ == "__main__":
    test_arryqueue()
