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
            self._listRef = preNode
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
        
'''
primary smith
CSCI-112
ECON-101
HIST-340
MATH-121

deleted smith
CSCI-112
ECON-101

lenght of smith
2

check whether not in
False

check whether in
True
'''
if __name__ == "__main__":
    test_sortedcircularlinkedlist()
