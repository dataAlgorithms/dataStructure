def findMiddle(head):

    ptr1x  = ptr2x = head
    i = 0
    # keep looping until we reach the tail(next will be None for the last node)
    if head is not None:
        while ptr1x.next is not None:
            if i == 0:
                ptr1x = ptr1x.next # increment only the lst pointer
                i = 1
            elif i == 1:
                ptr1x = ptr1x.next #increment both pointers
                ptr2x = ptr2x.next
                i = 0

        print 'Middle node:', ptr2x.data # now return the ptr2 which points to the middle node
    else:
        print 'Empty list, no middle node!'
        print '\r'

def findMiddleNew(head):
    
    slow_ptr = head
    fast_ptr = head 
    
    if head is  not None:
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next 
            slow_ptr = slow_ptr.next
            
        print 'The middle node:', slow_ptr.data
    else:
        print 'The linked list is empty, no middle node'
        print '\r'
        
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
  
def main():

    stl = SingleLinkedList() 
    findMiddleNew(stl._head)
    
    stl = SingleLinkedList() 
    stl.listNodeInsert(1, 0)
    stl.listNodeInsert(2, 0)
    stl.listNodeInsert(3, 0)        
    stl.listTraversal()
    findMiddleNew(stl._head)
    stl.listClear()
    stl.listTraversal()
 
    stl = SingleLinkedList() 
    stl.listNodeInsert(1, 0)
    stl.listNodeInsert(2, 0)
    stl.listNodeInsert(3, 0)      
    stl.listNodeInsert(4, 0)  
    stl.listTraversal()
    findMiddleNew(stl._head)
    stl.listClear()
    stl.listTraversal()
     
'''
Use findMiddle
Empty list, no middle node!

3  2  1  
Middle node: 2

4  3  2  1  
Middle node: 3

Using findMiddleNew
The linked list is empty, no middle node

3  2  1  
The middle node: 2

4  3  2  1  
The middle node: 2
'''
if __name__ == '__main__':  
    main()  
