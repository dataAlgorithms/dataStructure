def printList(head):
    
    while head is not None:
        print '%s ' % head.data,
        head = head.next 
        
def reverseBlock(head, k):
    current = head 
    next_  = None
    prev = None
    count = 0
     
    # Reverse first k nodes of the linked list
    while(current is not None and count < k):
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
        count += 1

    # next is now a pointer to (k+1)th node
    # recursively call for the list starting
    # from current . And make rest of the list as
    # next of first node
    if next_ is not None:
        head.next = reverseBlock(next_, k)

    # prev is new head of the input list
    return prev

class _SingleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class _SingleLinkedListIter:
    def __init__(self, head):
        self.curNode = head 
    def __iter__(self):
        return self
    def next(self):
        if self.curNode is not None:
            curNode = self.curNode 
            self.curNode = self.curNode.next 
            return curNode.data 
        else:
            raise StopIteration
    
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._count = 0

    # Get the length of single linked list
    def __len__(self):  
        return self._count
    
    # Get the length of single linked list
    def listLength(self):  
        return self._count

    # Check whether the sinlge linked list is empty
    def listIsEmpty(self):
        return self.listLength() == 0

    # Insert node into single linked list  
    def listNodeInsertBak(self, data, position):
        
        newNode = _SingleLinkedListNode(data)
        if position == 0: # insert a node at the front
            newNode.next = self._head 
            self._head = newNode 
        elif position == -1: # insert a node at the end
            preNode = self._head
            curNode = self._head 
            while curNode is not None:
                preNode = curNode 
                curNode = curNode.next 
                
            preNode.next = newNode 
        else: # insert a node at middle
            listLen = self.listLength()
            assert position >= 1 and position <= listLen, \
                "position:%s is out of list length:%s" % (position, listLen)
                
            preNode = self._head 
            curNode = self._head
            index = 0 
            while curNode is not None and index < position:
                preNode = curNode 
                curNode = curNode.next 
                index += 1
                
            newNode.next = curNode 
            preNode.next = newNode 
            
        self._count += 1

    def listNodeInsert(self, data, position):
        assert position >= -1 and position <= len(self), \
             "Position is out of list length."
        newNode = _SingleLinkedListNode(data)
        if len(self) == 1:
            assert position == 0 or position == -1, \
                "position is out of range!"
            if position == 0:
                newNode.next = self._head 
                self._head = newNode
            elif position == -1:
                self._head.next = newNode  
                newNode.prev = self._head
        else:        
            if position == 0:
                if self.listIsEmpty():
                    self._head = newNode 
                else:
                    newNode.next = self._head
                    self._head = newNode
            elif position == -1:
                preNode = self._head
                curNode = self._head
                while curNode is not None:
                    preNode = curNode
                    curNode = curNode.next

                preNode.next = newNode
            else:                 
                preNode = self._head
                curNode = self._head
                index = 0
                while curNode.next is not None and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                newNode.next = curNode
                preNode.next = newNode

        self._count += 1    
                        
    # Delete node from single linked list
    def listNodeDelete(self, position):
        
        assert not self.listIsEmpty(), "Single linked list is empty!"
        if self.listLength() == 1:
            assert position == 0 or position == -1, "position should be 0 or -1 when list length is 1!"
            self._head = None
        else:
            if position == 0:
                self._head = self._head.next 
            elif position == -1:
                preNode = self._head 
                curNode = self._head 
                while curNode.next is not None:
                    preNode = curNode 
                    curNode = curNode.next 
                
                preNode.next = curNode.next 
            else:
                preNode = self._head 
                curNode = self._head 
                index = 0
            
                assert position >=1 and position < self.listLength(), \
                   "positon:%s is out of list length:%s" % (position, self.listLength())
                while curNode.next is not None and index < position:
                    preNode = curNode 
                    curNode = curNode.next 
                    index += 1
                
                preNode.next = curNode.next    
            
        self._count -= 1

    def listTraversal(self):
        curNode = self._head 
        while curNode is not None:
            print "%s " % curNode.data,
            curNode = curNode.next 
        print '\r'

    def listClear(self):
        listLen = self.listLength()
        for _ in range(listLen):
            self.listNodeDelete(0)

    def __iter__(self):
        return _SingleLinkedListIter(self._head)
  
def main():
  
    print ':::reverse block of 2 node'
    stl = SingleLinkedList()
  
    for i in range(10, 0, -1):
        stl.listNodeInsert(i, 0)  
    stl.listTraversal()

    newHead = reverseBlock(stl._head, 2)
    printList(newHead)
    
    print '\r\r:::reverse block of 3 node'
    stl = SingleLinkedList()
  
    for i in range(10, 0, -1):
        stl.listNodeInsert(i, 0)  
    stl.listTraversal()

    newHead = reverseBlock(stl._head, 3)
    printList(newHead)
    
    print '\r\r:::reverse block of 4 node'
    stl = SingleLinkedList()
  
    for i in range(10, 0, -1):
        stl.listNodeInsert(i, 0)  
    stl.listTraversal()

    newHead = reverseBlock(stl._head, 4)
    printList(newHead)

'''
:::reverse block of 2 node
1  2  3  4  5  6  7  8  9  10  
2  1  4  3  6  5  8  7  10  9  

:::reverse block of 3 node
1  2  3  4  5  6  7  8  9  10  
3  2  1  6  5  4  9  8  7  10  

:::reverse block of 4 node
1  2  3  4  5  6  7  8  9  10  
4  3  2  1  8  7  6  5  10  9 
'''
if __name__ == '__main__':  
    main()  
