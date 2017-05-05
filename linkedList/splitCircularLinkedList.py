'''
Problem:
Split a Circular linked list into two equal parts
  If the number of nodes in the list are odd then
    make first list one node extra than second list
    
Algorithm:
1. Store the mid and last pointers of the circular linked list using 
   Floyd cycle finding algorithms
2. Make the second half circular
3. Make the first half circular
4. Set head pointers of the two linked lists
'''
def splitCircularLinkedList(head):

    slowPtr = head
    fastPtr = head

    if head is None:
        return

    '''
    If there are odd nodes in the circurlar list then fastPtr.next becomes
    head and for even nodes fastPtr.next.next becomes head
    '''
    while fastPtr.next != head and fastPtr.next.next != head:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    # If there are even elements in list then move fastPtr
    if fastPtr.next.next == head:
        fastPtr = fastPtr.next

    # Set the head pointer of first  half
    head1 = head

    # Set the head pointer of second half
    if head.next != head:
        head2 = slowPtr.next

    # Make second half circular
    fastPtr.next = slowPtr.next

    # Make first half circular
    slowPtr.next = head

    # Return head1, head2
    return head1, head2

# Traversal Circular linked list
def printCLL(head):

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
 
    print '::Even circular linked list'
    cll = CircularLinkedList()
   
    cll.listNodeInsert(40, 0)
    cll.listNodeInsert(7, 0)
    cll.listNodeInsert(15, 0)    
    cll.listNodeInsert(4, 0)     
    cll.listTraversal()

    head1, head2 = splitCircularLinkedList(cll._listRef)
    print '\r:first half:'
    printCLL(head1)
    
    print '\r:second half:'
    printCLL(head2)
    
    print '\r\r::Odd circular linked list'
    cll = CircularLinkedList()
   
    cll.listNodeInsert(40, 0)
    cll.listNodeInsert(7, 0)
    cll.listNodeInsert(15, 0)    
    cll.listNodeInsert(4, 0)  
    cll.listNodeInsert(1, 0)     
    cll.listTraversal()

    head1, head2 = splitCircularLinkedList(cll._listRef)
    print '\r:first half:'
    printCLL(head1)
    
    print '\r:second half:'
    printCLL(head2)
    
'''
::Even circular linked list
4  15  7  40  

:first half:
4 15 
:second half:
7 40 

::Odd circular linked list
1  4  15  7  40  

:first half:
1 4 15 
:second half:
7 40
'''
if __name__ == '__main__':  
    main()  
