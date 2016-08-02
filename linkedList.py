1. Single Linked list
class LinkedList:
    # Init
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, item):
        newNode = _LinkedListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, item):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "curNode is not exist"
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        self._size -= 1

        return curNode.item

    def __iter__(self):
        return _LinkedListIter(self._head)

class _LinkedListNode:
    # Init
    def __init__(self, item):
        self.item = item
        self.next = None

class _LinkedListIter:
    # Init
    def __init__(self, head):
        self._curNode = head
    def __iter__(self):
        return self
    def next(self):
        if self._curNode is not None:
            node = self._curNode.item
            self._curNode = self._curNode.next
            return node
        else:
            raise StopIteration

def test_linkedList():
    
    # init a set named smith
    smith = LinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = LinkedList()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
    
    print '\r\rroberts: '
    for item in roberts:
        print item,
        
    print '\r\rremove ECON-101 of smith'
    smith.remove('ECON-101')

    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rremove MATH-121 of smith'
    smith.remove('MATH-121')
            
    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rin check'
    print 'HIST-340' in smith 
    print 'MATH-121' in smith
    
if __name__ == "__main__":
    test_linkedList()
    
2. both linked list
class LinkedList:
    # Init
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __length__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def __contains__(self, item):
        curNode = self._front
        while curNode is not None and curNode.item != item:
            curNode = curNode.next
        
        return curNode is not None
    
    def add(self, item):
        newNode = _LinkedListNode(item)
        if self._front is None:
            self._front = newNode
            self._back = newNode
            self._size += 1
        else:
            self._back.next = newNode
            self._back = newNode
            self._size += 1

    def remove(self, item):
        assert not self.isEmpty(), "Linked list is empty."
        preNode = None
        curNode = self._front
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next
        
        assert curNode.item == item, "item is not exits"
        preNode.next = curNode.next
        
        if curNode == self._back:
            self._back = preNode

        self._size -= 1

    def __iter__(self):
        return _LinkedListIter(self._front)

class _LinkedListIter:
    # Init
    def __init__(self, front):
        self._curNode = front
    def __iter__(self):
        return self
    def next(self):
        if self._curNode is not None:
            theItem = self._curNode.item
            self._curNode = self._curNode.next
            return theItem
        else:
            raise StopIteration

class _LinkedListNode:
    # Init
    def __init__(self, item):
        self.item = item
        self.next = None
        
def test_linkedListBag():
    
    # init a set named smith
    smith = LinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = LinkedList()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
    
    print '\r\rroberts: '
    for item in roberts:
        print item,
        
    print '\r\rremove ECON-101 of smith'
    smith.remove('ECON-101')

    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rremove MATH-121 of smith'
    smith.remove('MATH-121')
            
    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rin check'
    print 'HIST-340' in smith 
    print 'MATH-121' in smith
    
'''
smith: 
CSCI-112 MATH-121 HIST-340 ECON-101 

roberts: 
POL-101 ANTH-230 CSCI-112 ECON-101 

remove ECON-101 of smith


smith: 
CSCI-112 MATH-121 HIST-340 

remove MATH-121 of smith


smith: 
CSCI-112 HIST-340 

in check
True
False

'''
if __name__ == "__main__":
    test_linkedListBag()

3. double linked list
class DoubleSortedLinkedList:
    # Init
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    # Length
    def __len__(self):
        return self._size
    # IsEmpty
    def isEmpty(self):
        return self._size == 0
    # Contains
    def __contains__(self, item):
        if self._head is None:
            return False
        else:
            curNode = self._head
            while curNode is not None and curNode.value != item:
                curNode = curNode.next
            if curNode is None:
                return False
            else:
                return curNode.value == item 
        
    # Add
    def add(self, item):
        newnode = _DLinkListNode(item)
        if self._head is None:
            self._head = newnode
            self._tail = newnode
        elif item < self._head.value:
            newnode.next = self._head
            self._head.prev = newnode
            self._head = newnode
        elif item > self._tail.value:
            self._tail.next = newnode
            newnode.prev = self._tail
            self._tail = newnode
        else:
            node = self._head
            while self._head is not None and node.value < item:
                node = node.next

            newnode.next = node
            newnode.prev = node.prev
            node.prev.next = newnode
            node.prev = newnode

        self._size += 1
    # Remove
    def remove(self, item):
        assert item in self, "item is not in"
        if self._head is None:
            return False
        elif item == self._head.value:
            self._head = self._head.next
        elif item == self._tail.value:
            self._tail = self._tail.prev
        else:
            curNode = self._head
            while curNode is not None and curNode.value != item:
                curNode = curNode.next
            curNode.next.prev = curNode.prev
            curNode.prev.next = curNode.next
        self._size -= 1
    # Iter
    def __iter__(self):
        return _DLinkListIter(self._head)

# Double Linked list Iter
class _DLinkListIter:
    # Init
    def __init__(self, head):
        self._curNode = head
    def __iter__(self):
        return self
    def next(self):
        if self._curNode != None:
            value = self._curNode.value
            self._curNode = self._curNode.next
            return value
        raise StopIteration

# Double Linked list node
class _DLinkListNode:
    # Init
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

def test_sorteddoublelinkedlist():
    
    # init a linkedlist named smith
    smith = DoubleSortedLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    # print smith
    print 'primary smith'
    for item in smith:
        print item
        
    # remove one item
    smith.remove('HIST-340')
    
    # print smith
    print '\ndeleted smith'
    for item in smith:
        print item
        
    # pring length
    print '\nlenght of smith'
    print len(smith)
    
    # check whether not in
    print '\ncheck whether not in'
    print 'abc' in smith
 
    # check whether in
    print '\ncheck whether in'
    print 'ECON-101' in smith       
        
'''
primary smith
CSCI-112
ECON-101
HIST-340
MATH-121

deleted smith
CSCI-112
ECON-101
MATH-121

lenght of smith
3

check whether not in
False

check whether in
True

'''
if __name__ == "__main__":
    test_sorteddoublelinkedlist()
