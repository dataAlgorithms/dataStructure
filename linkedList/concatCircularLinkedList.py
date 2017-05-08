# Concat two Circular linked list
def concatList(last1, last2):

    if last1 is None:
        last1 = last2
        return last1.next

    if last2 is None:
        return last1.next

    ptr = last1.next
    last1.next = last2.next
    last2.next = ptr
    last1 = last2
    return last1.next

# Get the last node
def getLastNode(head):

    if head is None:
        return None

    preNode = head
    curNode = head.next
    if head is not None:
        while True:
            if curNode == head:
                return preNode

            preNode = curNode
            curNode = curNode.next

# Traversal Circular linked list
def printList(head):

    temp = head
    if head is not None:
        while True:
            print "%s" % temp.data,
            temp = temp.next
            if temp == head:
                break

class _CircularLinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class _CircularLinkedListIter:
    def __init__(self, listRef, count):
        self._listRef = listRef
        self._index = 0
        self._count = count 
    def __iter__(self):
        return self
    def next(self):
        if self._index < self._count:
            curNode = self._listRef.data
            self._listRef = self._listRef.next
            self._index += 1
            return curNode
        else:
            raise StopIteration

class CircularLinkedList:
    def __init__(self):
        self._listRef = None
        self._count = 0

    def __len__(self):
        return self._count

    def listLength(self):
        return self._count
    
    def listIsEmpty(self):
        return self._count == 0

    def listNodeInsert(self, data, position):
        newNode = _CircularLinkedListNode(data)
        
        if position == 0:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
                self._listRef = newNode
            else:
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next
                newNode.next = self._listRef
                curNode.next = newNode
                self._listRef = newNode
            
        elif position == -1:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
            else:                
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next
                curNode.next = newNode
                newNode.next = self._listRef
        else:
            if len(self) == 0:
                self._listRef = newNode 
                newNode.next = self._listRef
            elif len(self) == 1:
                curNode = self._listRef
                newNode.next = self._listRef
                self._listRef.next = newNode 
                self._listRef = newNode
            else:               
                preNode = self._listRef
                curNode = self._listRef
                index = 0
                while curNode.next is not self._listRef and index < position:
                    preNode  = curNode
                    curNode = curNode.next
                    index += 1
        
                newNode.next = curNode
                preNode.next = newNode

        self._count += 1

    def listNodeDelete(self, position):
        assert position >= -1 and position < len(self), \
                  "Out of subcription!"
        assert not self.listIsEmpty(), "List is empty!"
        if len(self) == 1:
            self._listRef = None
        else:
            if position == 0:
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    curNode = curNode.next

                self._listRef = self._listRef.next
                curNode.next = self._listRef
            elif position == -1:
                preNode = self._listRef
                curNode = self._listRef
                while curNode.next is not self._listRef:
                    preNode = curNode
                    curNode = curNode.next
                
                preNode.next = self._listRef
            else:
                preNode = self._listRef
                curNode = self._listRef
                index = 0
                while curNode.next is not self._listRef and index < position:
                    preNode = curNode
                    curNode = curNode.next
                    index += 1

                preNode.next = curNode.next

        self._count -= 1

    def listTraversal(self):
        index = 0
        curNode = self._listRef
        
        while index < len(self):
            print "%s " % curNode.data,
            curNode = curNode.next
            index += 1

        print "\r"
        
    def __iter__(self):
        return _CircularLinkedListIter(self._listRef, len(self))
    
def main():

    print ':::Init two circular linked list'  
    cll = CircularLinkedList()
    cll.listNodeInsert(1, 0)
    cll.listNodeInsert(2, 0)
    cll.listNodeInsert(3, 0)        
    cll.listTraversal()
    
    cll1 = CircularLinkedList()
    cll1.listNodeInsert(4, 0)
    cll1.listNodeInsert(5, 0)
    cll1.listNodeInsert(6, 0)        
    cll1.listTraversal()

    print '\r:::Get the last ndoe of circular linked list'
    last1 = getLastNode(cll._listRef)
    last2 = getLastNode(cll1._listRef)

    print 'last1:', last1.data 
    print 'last2:', last2.data
    
    print '\r:::Concat the two circurlar linked list'
    last = concatList(last1, last2)
    printList(last)
    
'''
:::Init two circular linked list
3  2  1  
6  5  4  

:::Get the last ndoe of circular linked list
last1: 1
last2: 4

:::Concat the two circurlar linked list
3 2 1 6 5 4
'''
if __name__ == '__main__':  
    main()  
