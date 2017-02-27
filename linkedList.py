1. Single Linked list
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __length__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, item):
        newNode = SingleLinkedListNode(item)
        newNode.next = self._head
        self._head = newNode

        self._size += 1

    def insert(self, item, position):
        if position == 0:
            # insert at the beginning
            newNode = SingleLinkedListNode(item)
            newNode.next = self._head
            self._head = newNode

            self._size += 1

        elif position == -1:
            # insert at the ending
            newNode = SingleLinkedListNode(item)
            
            preNode = self._head
            curNode = self._head
            while curNode is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = newNode
            
            self._size += 1

        else:
            # insert at the middle
            newNode = SingleLinkedListNode(item)
            if self._head is None:
                self._head  = newNode
                self._size += 1

            else:
                curNode = self._head
                preNode = self._head
                index = 0
                while curNode is not None and index != position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                newNode.next = curNode
                preNode.next = newNode
                self._size += 1

    def removePos(self, position):
        assert not self.isEmpty(), "LinkedList is empty!"
        if position == 0:
            # remove the first item
            self._head = self._head.next
            self._size -= 1
        elif position == -1:
            # remove the last item
            preNode = self._head
            curNode = self._head
            while curNode.next is not None:
                preNode = curNode
                curNode = curNode.next

            preNode.next = None
            self._size -= 1

        else:
            # remove the middle item
            preNode = self._head
            curNode = self._head
            index = 0
            while curNode is not None and index != position:
                preNode = curNode
                curNode = curNode.next

                index += 1

            preNode.next = curNode.next
            self._size -= 1

    def remove(self, item):
        assert not self.isEmpty(), "Linkedlist is empty!"
        preNode = self._head 
        curNode = self._head 
        while curNode is not None and curNode.item !=  item:
            preNode = curNode 
            curNode = curNode.next 
            
        assert curNode.item is not None, "item is not in!"
        if curNode is self._head:
            self._head = self._head.next 
        else:
            preNode.next = curNode.next 
        
        self._size -= 1
            
    def __iter__(self):
        return SingleLinkedListIer(self._head)

class SingleLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        
class SingleLinkedListIer:
    def __init__(self, head):
        self._head = head 
    def __iter__(self):
        return self 
    def next(self):
        if self._head is not None:
            curNode = self._head.item 
            self._head = self._head.next 
            return curNode 
        else:
            raise StopIteration
    
'''
smith: 
ECON-101 HIST-340 MATH-121 CSCI-112 

roberts: 
ECON-101 CSCI-112 ANTH-230 POL-101 

remove ECON-101 of smith


smith: 
HIST-340 MATH-121 CSCI-112 

remove MATH-121 of smith


smith: 
HIST-340 CSCI-112 

in check
True
False


insert pos check


smith: 
nihao HIST-340 CSCI-112 

smith: 
nihao HIST-340 CSCI-112 nihao 

smith: 
nihao HIST-340 nihao CSCI-112 nihao 

remove pos check


smith: 
HIST-340 nihao CSCI-112 nihao 

smith: 
HIST-340 nihao CSCI-112 

smith: 
HIST-340 CSCI-112
'''    
def test_linkedList():
    
    # init a set named smith
    smith = SingleLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = SingleLinkedList()
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
    
    print '\r\rinsert pos check'
    item = 'nihao'
    smith.insert(item, 0)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    item = 'nihao'
    smith.insert(item, -1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
                
    item = 'nihao'
    smith.insert(item, 2)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    print '\r\rremove pos check'
    item = 'nihao'
    smith.removePos(0)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
        
    item = 'nihao'
    smith.removePos(-1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,    
                
    item = 'nihao'
    smith.removePos(1)
    
    print '\r\rsmith: '
    for item in smith:
        print item,   
            
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

4. circular linked list
class CircularSortedLinkedList:
    # Init
    def __init__(self):
        self._listRef = None
        self._size = 0
    # Length
    def __len__(self):
        return self._size
    # Check whether the list is empty
    def isEmpty(self):
        return self._size == 0
    # Check whether the item in the list
    def __contains__(self, item):
        curNode = self._listRef
        done = self._listRef is None 
        while not done:
            curNode = curNode.next
            if curNode.value == item:
                return True 
            else:
                done = curNode is self._listRef or curNode.value > item
                
        return False

    # Add operation
    def add(self, item):
        newnode = _DLinkListNode(item)
        if self._listRef is None:
            self._listRef = newnode
            newnode.next = newnode
        elif item < self._listRef.next.value:
            newnode.next = self._listRef.next
            self._listRef.next = newnode
        elif item > self._listRef.value:
            newnode.next = self._listRef.next
            self._listRef.next = newnode
            self._listRef = newnode
        else:
            preNode = None
            curNode = self._listRef
            done = self._listRef is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef or curNode.value > item
            newnode.next = curNode
            preNode.next = newnode
        self._size += 1
        
    # Remove operation
    def remove(self, item):
        assert item in self, "item is not in"
        
        if self._listRef is None:
            return False
        elif item == self._listRef.next.value:
            self._listRef.next = self._listRef.next.next
        elif item == self._listRef.value:
            preNode = None
            curNode = self._listRef
            done = self._listRef is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef
            preNode.next = self._listRef.next
            self._listRef = preNode
        else:
            preNode = None
            curNode = self._listRef.next
            done = self._listRef  is None
            while not done:
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._listRef or curNode.value == item
            preNode.next = curNode.next
        self._size -= 1
    # Iter
    def __iter__(self):
        return _CircularSortedLinkedListIter(self._listRef, self._size)

# Iter
class _CircularSortedLinkedListIter:
    # Init
    def __init__(self, listRef, size):
        self._curNode = listRef.next
        self._size = size 
        self._cIndex = 0
    def __iter__(self):
        return self
    def next(self):
        if self._cIndex < self._size:
            value = self._curNode.value
            self._curNode = self._curNode.next
            self._cIndex += 1
            return value
        else:
            raise StopIteration

# Node
class _DLinkListNode:
    # Init
    def __init__(self, item):
        self.value = item
        self.next = None
        
def test_sortedcircularlinkedlist():
    
    # init a linkedlist named smith
    smith = CircularSortedLinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    # print smith
    print 'primary smith'
    for item in smith:
        print item
        
    # remove one item
    smith.remove('MATH-121')
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
    
    # delete all
    smith.remove('CSCI-112')
    smith.remove('ECON-101')
    
    for item in smith:
        print item
        
if __name__ == "__main__":
    test_sortedcircularlinkedlist()
