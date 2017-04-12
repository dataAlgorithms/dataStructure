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
