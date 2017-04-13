'''
Input : Head of following linked list  
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

Input : Head of following linked list  
       1->2->3->4->5->NULL
Output : Linked list should be changed to,
       5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL
'''

# Utility function to print the linked LinkedList
def printList(head):
    temp = head
    while(temp):
        print "%s " % temp.data,
        temp = temp.next
    print '\r'
            
# Reverse a single linked list using iterative version
'''
Iterate trough the linked list. In loop, change next to prev, prev to current and current to next.
'''
def reverseListIter(head):

    prev = None
    nextNode = None
    while head is not None:
        nextNode = head.next
        head.next = prev
        prev = head
        head = nextNode

    return prev

# Reverse a single linked list using recursive way
'''
1) Divide the list in two parts - first node and rest of the linked list.
2) Call reverse for the rest of the linked list.
3) Link rest to first.
4) Fix head pointer
'''
def reverseListRecur(head):

    if head is None:
        return None

    if head.next is None:
        return head

    secondElem = head.next

    # Need to unlink list from the rest or you will get a cycle
    head.next = None
    # Reverse everything from the second element on
    reverseRest = reverseListRecur(secondElem)
    secondElem.next = head # then we join the two  list

    return reverseRest
    
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

    # Function to reverse the linked list
    def listReverseIter(self):
        prev = None
        current = self._head
        while(current is not None):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self._head = prev
        
    def reverseUtil(self, curr, prev):
    
        # If last node mark it head
        if curr.next is None:
            self._head = curr
    
            # Update next to prev node
            curr.next = prev
            return
    
        # Save curr.next node for recursive call
        next_ = curr.next
    
        # And update next
        curr.next = prev
    
        self.reverseUtil(next_, curr)
    
    # This function mainly calls reverseUtil with previous as None
    def listReverseRecu(self):
        if self._head is None:
            return
        self.reverseUtil(self._head, None)
        
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
  
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self._head
        while(temp):
            print temp.data,
            temp = temp.next
            
def main():
 
        stl = SingleLinkedList() 
        stl.listNodeInsert(1, 0)
        stl.listNodeInsert(2, 0)
        stl.listNodeInsert(3, 0)       
        stl.listTraversal()
        stl.listReverseIter()
        stl.listTraversal()
        stl.listReverseIter()
        stl.listTraversal()
        stl.listReverseRecu()
        stl.listTraversal()
        
        head = reverseListIter(stl._head)  
        printList(head)
                        
        head = reverseListRecur(head)
        printList(head)

'''
3  2  1  
1  2  3  
3  2  1  
1  2  3  
3  2  1  
1  2  3  
'''        
if __name__ == '__main__':  
    main()  
