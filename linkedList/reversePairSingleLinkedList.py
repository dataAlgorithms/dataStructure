# Reverse pair of single Linked List using recursive way
def reversePairRecu(head):

    temp = None
    if head is None:
        return 
    elif head.next is None: # base case for empty or 1 element list
        return head
    else:
        # Reverse first pair
        temp = head.next
        head.next = temp.next
        temp.next = head
        head = temp

        # Call the method recursively for the rest of the list
        head.next.next = reversePairRecu(head.next.next)
        return head

# Reverse pair of single Linked List using iterative way
def reversePairIter(head):

    temp1 = None
    temp2 = None
    current = head

    while current is not None and current.next is not None:
        if temp1  is not None:
            temp1.next.next = current.next

        temp1 = current.next
        current.next = current.next.next
        temp1.next = current
       
        if temp2 is None:
            temp2 = temp1

        current = current.next

    return temp2

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
    
    print '::Create st1'
    stl = SingleLinkedList()
    stl.listNodeInsert(5, 0)
    stl.listNodeInsert(4, 0)
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(2, 0)
    stl.listNodeInsert(1, 0)  
    stl.listTraversal()
    
    print '\r:::Reverse pair using recursive way'
    head = reversePairRecu(stl._head)
    while head is not None:
        print head.data, 
        head = head.next

    print '\r\r::Create st11'
    stl1 = SingleLinkedList()
    stl1.listNodeInsert(5, 0)
    stl1.listNodeInsert(4, 0)
    stl1.listNodeInsert(3, 0)
    stl1.listNodeInsert(2, 0)
    stl1.listNodeInsert(1, 0)  
    stl1.listTraversal()
    
    print '\r:::Reverse pair using recursive way'
    head = reversePairIter(stl1._head)
    while head is not None:
        print head.data, 
        head = head.next
         
'''
::Create st1
1  2  3  4  5  

:::Reverse pair using recursive way
2 1 4 3 5 

::Create st11
1  2  3  4  5  

:::Reverse pair using recursive way
2 1 4 3 5
'''       
if __name__ == '__main__':  
    main()  
