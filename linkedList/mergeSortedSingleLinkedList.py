def mergeSortedListRec(head1, head2):

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = mergeSortedListRec(head1.next, head2)
        return head1
    else:
        head2.next = mergeSortedListRec(head2.next, head1)
        return head2

def mergeSortedListIter(head1, head2):

    newNode = _SingleLinkedListNode(None)
    temp = newNode
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        else:
            temp.next = head2
            temp = temp.next
            head2 = head2.next

    if head1 is not None:
        temp.next = head1
    else:
        temp.next = head2

    temp = newNode.next
    return temp

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
    stl.listNodeInsert(3, 0)
    stl.listNodeInsert(2, 0)
    stl.listNodeInsert(1, 0)  
    stl.listTraversal()
        
    print '\r:::Create stl1'
    stl1 = SingleLinkedList()
    stl1.listNodeInsert(6, 0)
    stl1.listNodeInsert(5, 0)
    stl1.listNodeInsert(4, 0)  
    stl1.listTraversal()
    
    print '\r:::Merge using iter'
    result = mergeSortedListIter(stl._head, stl1._head)
    while result is not None:
        print result.data,
        result = result.next
        
    print '\r\r::Create stl2'
    stl2 = SingleLinkedList()
    stl2.listNodeInsert(3, 0)
    stl2.listNodeInsert(2, 0)
    stl2.listNodeInsert(1, 0)  
    stl2.listTraversal()
        
    print '\r:::Create stl3'
    stl3 = SingleLinkedList()
    stl3.listNodeInsert(6, 0)
    stl3.listNodeInsert(5, 0)
    stl3.listNodeInsert(4, 0)  
    stl3.listTraversal()
    
    print '\r:::Merge using recur'
    result1 = mergeSortedListRec(stl2._head, stl3._head)
    while result1 is not None:
        print result1.data,
        result1 = result1.next
        
'''
::Create st1
1  2  3  

:::Create stl1
4  5  6  

:::Merge using iter
1 2 3 4 5 6 

::Create stl2
1  2  3  

:::Create stl3
4  5  6  

:::Merge using recur
1 2 3 4 5 6
'''
if __name__ == '__main__':  
    main()  
