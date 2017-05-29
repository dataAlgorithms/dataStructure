'''
Question:
Segregate even and odd nodes in a Linked List
Given a Linked List of integers, write a function to modify the 
linked list such that all even numbers appear before all the odd numbers 
in the modified linked list. Also, keep the order of even and odd numbers same.

Algorithms:
The idea is to split the linked list into two: 
one containing all even nodes and other containing all odd nodes. 
And finally attach the odd node linked list after the even node linked list.
To split the Linked List, traverse the original Linked List and move all 
odd nodes to a separate Linked List of all odd nodes. At the end of loop, 
the original list will have all the even nodes and the odd node list will 
have all the odd nodes. To keep the ordering of all nodes same, we must 
insert all the odd nodes at the end of the odd node list. And to do that 
in constant time, we must keep track of last pointer in the odd node list.

Time:
O(n)

Refer:
http://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/
'''
def exchangeEvenOddList(head):
    
    # Initializing the odd and even list headers
    oddList = None
    evenList = None

    # Creating tail variabls for both the list
    oddListEnd = None
    evenListEnd = None
    itr = head

    if head is None:
        return
    else:
        while itr is not None:
            if itr.data % 2 == 0:
                if evenList is None:
                    # first even node
                    evenList = evenListEnd = itr
                else:
                    evenListEnd.next = itr
                    evenListEnd = itr
            else:
                if oddList is None:
                    # first odd node
                    oddList = oddListEnd = itr
                else:
                    # inserting the node at the end of linked list
                    oddListEnd.next = itr
                    oddListEnd = itr
            itr = itr.next

    if oddList is None or evenList is None:
        return head
        
    evenListEnd.next = oddList
    oddListEnd.next = None
    head = evenList
    return head

def printList(head):
    
    while head is not None:
        print '%s ' % head.data, 
        head = head.next
        
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
    
    # Get the item
    def __getitem__(self, pos):
        assert pos >= -1 and pos < len(self), \
                "invalid position!"
        preNode = self._head
        curNode = self._head 
        index = 0
        while curNode is not None and index < pos:
            preNode = curNode
            curNode = curNode.next 
            index += 1
            
        return preNode.data 
    
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
  
def test_exchange():

    print ':::Including even add odd numbers'
    stl = SingleLinkedList()
    for item in [6,7,1,4,5,10,12,8,15,17]:
        stl.listNodeInsert(item, 0)
    stl.listTraversal()    
    head = exchangeEvenOddList(stl._head)
    printList(head)
             
    print '\r\r:::Including even numbers'
    stl = SingleLinkedList()
    for item in [10,12,8]:
        stl.listNodeInsert(item, 0)
    stl.listTraversal()    
    head = exchangeEvenOddList(stl._head)
    printList(head)

    print '\r\r:::Including even numbers'
    stl = SingleLinkedList()
    for item in [7, 5, 3, 1]:
        stl.listNodeInsert(item, 0)
    stl.listTraversal()    
    head = exchangeEvenOddList(stl._head)
    printList(head)
        
    print '\r\r:::All even numbers before odd numbers'
    stl = SingleLinkedList()
    for item in [11,7,10,8,6,4,2,0]:
        stl.listNodeInsert(item, 0)
    stl.listTraversal()    
    head = exchangeEvenOddList(stl._head)
    printList(head)
    
    print '\r\r:::All odd numbers before even numbers'
    stl = SingleLinkedList()
    for item in [10,8,6,4,2,0,11,7]:
        stl.listNodeInsert(item, 0)
    stl.listTraversal()    
    head = exchangeEvenOddList(stl._head)
    printList(head)
    
'''
:::Including even add odd numbers
17  15  8  12  10  5  4  1  7  6  
8  12  10  4  6  17  15  5  1  7  

:::Including even numbers
8  12  10  
8  12  10  

:::Including even numbers
1  3  5  7  
1  3  5  7  

:::All even numbers before odd numbers
0  2  4  6  8  10  7  11  
0  2  4  6  8  10  7  11  

:::All odd numbers before even numbers
7  11  0  2  4  6  8  10  
0  2  4  6  8  10  7  11 
'''
if __name__ == '__main__':  
    test_exchange()  
